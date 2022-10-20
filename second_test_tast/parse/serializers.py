from rest_framework import serializers


class ParseSerializer(serializers.Serializer):
    url = serializers.CharField()
