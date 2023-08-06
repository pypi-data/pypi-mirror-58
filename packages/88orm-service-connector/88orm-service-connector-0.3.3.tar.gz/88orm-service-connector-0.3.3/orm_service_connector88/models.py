import json
from typing import Dict
from urllib.parse import urljoin

import requests
from django.conf import settings

# NOTE: All models info will be stored here.
# contains fields and related_names,
# keep note don't redefine the MODELS variable
# for keeping the reactivity. If you want to
# change the value, just clear or append it.
MODELS = []

service_settings = getattr(settings, 'ORM_SERVICE', {
    "url": "",
    "auth_header": ""
})
ORM_SERVICE_URL = service_settings.get("url")
ORM_SERVICE_AUTH_HEADER = service_settings.get("auth_header")


class VirtualModel(object):
    def __init__(
            self,
            model: str,
            payload: dict,
            value=None,
            model_info=None
    ):
        self._payload = payload
        app_label = None
        if len(model.split('.')) == 2:
            app_label, model = model.split('.')
        self.__model = model
        self._app_label = app_label
        self._attrs = {}
        if not model_info:
            model_info = get_model(model, app_label)
        if not app_label:
            self._app_label = model_info.get('app_label')
        self._fields = model_info.get('fields')  # type: Dict
        self._related_names = model_info.get('related_names')  # type: Dict
        if value:
            self._set_value(value)

    def __repr__(self):
        key = self._attrs.get('id') or self._attrs.get(next(iter(self._attrs)))
        model_name = self.__model
        if model_name.islower():
            model_name = model_name.capitalize()
        return f"<{model_name}: {key}>"

    def __setattr__(self, key, value):
        try:
            super(VirtualModel, self).__setattr__(key, value)
            if key in self._fields:
                self._attrs.update({
                    key: value
                })
        except Exception:
            pass

    def _set_attr_single_instance(self, key, value):
        from .connector import ORMServices

        attr_value = None
        if self._attrs.get(f"{key}_id"):
            related_model = value.get('related_model')
            model = f"{related_model.get('app_label')}.{related_model.get('name')}"
            attr_value = ORMServices(model)
        setattr(self, key, attr_value)

    def _set_related_attributes(self):
        from .connector import ORMServices

        for key, value in self._fields.items():
            if not hasattr(self, key):
                type_field = value.get('type')
                if type_field in ['ForeignKey', 'OneToOneField']:
                    self._set_attr_single_instance(key, value)
                elif type_field == 'ManyToManyField':
                    related_model = value.get('related_model')
                    model = f"{related_model.get('app_label')}.{related_model.get('name')}"
                    attr_value = ORMServices(model)
                    setattr(self, key, attr_value)

        for key, value in self._related_names.items():
            if not hasattr(self, key):
                related_model = value.get('related_model')
                model = f"{related_model.get('app_label')}.{related_model.get('name')}"
                attr_value = ORMServices(model)
                setattr(self, key, attr_value)

    def _set_value(self, attrs: Dict):
        self._attrs.update(attrs)
        for key, value in attrs.items():
            setattr(self, key, value)
        self._set_related_attributes()

    def get_related(self, name):
        from .connector import ORMServices

        attr = getattr(self, name)
        if isinstance(attr, ORMServices):
            if name in self._fields:
                field = self._fields.get(name)
                if field.get('type') in ['ForeignKey', 'OneToOneField']:
                    return attr.get(id=self._attrs.get(f"{name}_id"))
                elif field.get('type') == 'ManyToManyField':
                    key = field.get('related_model').get('related_query_name')
                    return attr.filter(**{key: self.id})
        return attr

    def reverse_related(self, related_name):
        try:
            orm = getattr(self, related_name)  # type: ORMServices
            rel = self._related_names.get(related_name)
            related_model = rel.get('related_model')
            filter_kwargs = {
                related_model.get('related_field'): self.id
            }
            if rel.get('type') == 'OneToOneRel':
                return orm.get(**filter_kwargs)
            return orm.filter(**filter_kwargs)
        except AttributeError:
            raise AttributeError(f'{self.__model} has no related {related_name}')

    def refresh_from_db(self):
        from .connector import ORMServices

        instance = ORMServices(
            model=self.__model,
            fields=list(self._attrs)
        )
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_queryset")
        attrs = instance._ORMServices__request_get(
            url=url,
            payload=self._payload
        )
        if isinstance(attrs, dict):
            for key, value in attrs:
                setattr(self, key, value)

    def save(self):
        from .connector import ORMServices

        instance = ORMServices(
            model=self.__model,
            fields=list(self._attrs)
        )
        payload = self._payload.copy()
        payload.get("payload").update({
            "save": self._attrs
        })
        return instance._save(payload)


class ModelNotFound(Exception):
    pass


class MultipleModelsReturned(Exception):
    pass


def initialize_models(force=False):
    global MODELS
    if not MODELS or force:
        url = urljoin(ORM_SERVICE_URL, "/api/v1/orm_services/get_models")
        response = requests.get(url, headers={
            "content-type": "application/json",
            'Authorization': ORM_SERVICE_AUTH_HEADER
        })
        if response.status_code == 400:
            raise Exception(response.text)
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            if response.text:
                raise Exception(response.text)
        else:
            MODELS.clear()
            MODELS += response


def get_model(name: str, app_label=None) -> Dict:
    initialize_models()
    name = name.lower()
    result = list(filter(
        lambda model: model.get('model') == name,
        MODELS
    ))
    if app_label:
        result = list(filter(
            lambda model: model.get('app_label') == app_label,
            result
        ))
    if not result:
        msg = f"Cannot find model {name}"
        if app_label:
            msg = f"{msg} with app_label {app_label}"
        raise ModelNotFound(msg)
    if len(result) > 1:
        multiple = list(map(lambda x: x.get('app_label'), result))
        raise MultipleModelsReturned(f"Please provide app_label: {multiple}")
    return result[0]
