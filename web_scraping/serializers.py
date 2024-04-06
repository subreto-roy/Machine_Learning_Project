from rest_framework import serializers

class ExtractionSchemaSerializer(serializers.Serializer):
    url = serializers.URLField()
    schema = serializers.JSONField()
