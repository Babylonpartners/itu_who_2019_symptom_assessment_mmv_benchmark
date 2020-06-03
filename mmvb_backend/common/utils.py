from uuid import uuid4

from django.conf import settings
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.status import HTTP_200_OK

import requests
from common.definitions import HealthCheckStatus
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from stringcase import camelcase

DEFAULT_TIMEOUT = settings.DEFAULT_TIMEOUT
DEFAULT_MAX_RETRIES = settings.MAX_RETRIES


class CamelCaseAutoSchema(AutoSchema):
    def map_serializer(self, serializer):
        result = super().map_serializer(serializer)
        camelized_properties = {
            camelcase(field_name): schema
            for field_name, schema in result["properties"].items()
        }
        new_result = {"type": "object", "properties": camelized_properties}
        if "required" in result:
            new_result["required"] = list(map(camelcase, result["required"]))

        return new_result


def is_true(value):
    return str(value).lower() in ["1", "true", "yes"]


def generate_id():
    return uuid4()


def perform_request(url, retries=DEFAULT_MAX_RETRIES, timeout=DEFAULT_TIMEOUT):
    adapter = HTTPAdapter(max_retries=1)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    response = {"status": "", "data": None, "detail": ""}

    try:
        request_response = session.get(url, timeout=timeout)
    except ConnectionError as exc:
        response["status"] = HealthCheckStatus.TIMEOUT
        response["detail"] = f"Error trying to perform request. Got {str(exc)}"
    except Exception as exc:
        response["status"] = HealthCheckStatus.BAD_RESPONSE
        response["detail"] = f"Error trying to perform request. Got {str(exc)}"
    else:
        if request_response.status_code != HTTP_200_OK:
            response["status"] = HealthCheckStatus.BAD_RESPONSE
        else:
            response["status"] = HealthCheckStatus.OK

        response["data"] = request_response.json()

    return response
