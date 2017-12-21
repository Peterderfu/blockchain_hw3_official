from rest_framework import serializers

class ApiSerializer(serializers.Serializer):
  def create(self, validated_data):
    return Api.objects.create(**validated_data)