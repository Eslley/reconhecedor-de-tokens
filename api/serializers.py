from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    input = serializers.CharField(required=True)