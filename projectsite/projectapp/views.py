from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_list_or_404
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from projectapp.models import Light
from projectapp.models import Video_Wall
from projectapp.models import Workstation
from projectapp.models import Display
from projectapp.models import Media
from projectapp.models import Preset

from projectapp.serialisers import LightSerializer
from projectapp.serialisers import Video_WallSerializer
from projectapp.serialisers import WorkstationSerializer
from projectapp.serialisers import DisplaySerializer
from projectapp.serialisers import MediaSerializer
from projectapp.serialisers import PresetSerializer

def index(request):
    return HttpResponse("This page can be used to test app functionality")

#API Endpoint Views
#All endpoints to be shown in Django Restframework API Interface

#Lights Endpoint
class LightsView(ListCreateAPIView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Lights Endpoint
class SingleLightView(RetrieveUpdateDestroyAPIView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

#Video Wall Endpoint
class Video_WallView(ListCreateAPIView):
    queryset = Video_Wall.objects.all()
    serializer_class = Video_WallSerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Video Wall Panels Endpoint
class SingleVideoWallPanelView(RetrieveUpdateDestroyAPIView):
    queryset = Video_Wall.objects.all()
    serializer_class = Video_WallSerializer

#Workstations Endpoint
class WorkstationView(ListCreateAPIView):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Workstations Endpoint
class SingleWorkstationView(RetrieveUpdateDestroyAPIView):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

#Displays Endpoint
class DisplayView(ListCreateAPIView):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Displays Endpoint
class SingleDisplayView(RetrieveUpdateDestroyAPIView):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer

#Media Endpoint
class MediaView(ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Media Endpoint
class SingleMediaView(RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

#Preset Endpoint
class PresetView(ListCreateAPIView):
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer

    def perform_create(self, serializer):
        return serializer.save()

#Individual Preset Endpoint
class SinglePresetView(RetrieveUpdateDestroyAPIView):
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer

