from rest_framework.schemas.openapi import AutoSchema
from stringcase import camelcase


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
