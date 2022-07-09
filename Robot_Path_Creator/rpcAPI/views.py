from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DestinationSerializer, PathSerializer
from .models import Destination, Path

# Create your views here.


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class PathViewSet(viewsets.ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer