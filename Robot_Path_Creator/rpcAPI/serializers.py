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