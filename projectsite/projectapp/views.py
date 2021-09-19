# from projectsite.projectapp.serialisers import Lights_GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_list_or_404
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status

from projectapp.models import Lights_Group
from projectapp.models import Lights
from projectapp.models import Video_Wall_Panel_Group
from projectapp.models import Video_Wall_Panel
from projectapp.models import Workstations

from projectapp.serialisers import Lights_GroupSerializer
from projectapp.serialisers import LightsSerializer
from projectapp.serialisers import Video_Wall_Panel_GroupSerializer
from projectapp.serialisers import Video_Wall_PanelSerializer
from projectapp.serialisers import WorkstationsSerializer

# Create your views here.
def index(request):
    return HttpResponse("This page can be used to test app functionality")

class Lights_GroupList(APIView):
    def get(self, request):
        Lights_Groups = Lights_Group.objects.all()
        serializer= Lights_GroupSerializer(Lights_Groups, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class LightsList(APIView):
    def get(self, request):
        Lights1 = Lights.objects.all()
        serializer= LightsSerializer(Lights1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class Video_Wall_Panel_GroupList(APIView):
    def get(self, request):
        Video_Wall_Groups = Video_Wall_Panel_Group.objects.all()
        serializer= Video_Wall_Panel_GroupSerializer(Video_Wall_Groups, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class Video_Wall_PanelList(APIView):
    def get(self, request):
        Video_Wall_Panels = Video_Wall_Panel.objects.all()
        serializer= Video_Wall_PanelSerializer(Video_Wall_Panels, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class WorkstationsList(APIView):
    def get(self, request):
        Workstations1 = Workstations.objects.all()
        serializer= WorkstationsSerializer(Workstations1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

