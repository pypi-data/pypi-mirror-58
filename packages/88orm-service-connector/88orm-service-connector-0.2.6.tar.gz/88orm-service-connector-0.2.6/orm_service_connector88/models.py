import json
from typing import Dict
from urllib.parse import urljoin

import requests
from django.conf import settings

# NOTE: All models info will be stored here.
# contains fields and related_names
MODELS = []

service_settings = getattr(settings, 'ORM_SERVICE', {
    "url": "",
    "auth_header": ""
})
ORM_SERVICE_URL = service_settings.get("url")
ORM_SERVICE_AUTH_HEADER = service_settings.get("auth_header")


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
