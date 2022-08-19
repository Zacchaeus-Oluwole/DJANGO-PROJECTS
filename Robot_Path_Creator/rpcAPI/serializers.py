from rest_framework import serializers
from .models import Path, Destination


class PathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Path
        fields = '__all__'

class DestinationSerializer(serializers.ModelSerializer):
    direction = PathSerializer(many = True)

    class Meta:
        model = Destination
        fields = '__all__'

    # def create(self, validated_data):
    #     # direction = validated_data.pop()
    #     # destination_instance = Destination.objects.create(**validated_data)
    #     # for dir in direction:
    #     #     Path.objects.create(destination = destination_instance, **dir)
    #     return destination_instance