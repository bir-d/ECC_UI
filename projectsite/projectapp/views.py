# from projectsite.projectapp.serialisers import Lights_GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_list_or_404
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status

from projectapp.models import Light_Group
from projectapp.models import Light
from projectapp.models import Video_Wall_Panel_Group
from projectapp.models import Video_Wall_Panel
from projectapp.models import Workstation

from projectapp.serialisers import Light_GroupSerializer
from projectapp.serialisers import LightSerializer
from projectapp.serialisers import Video_Wall_Panel_GroupSerializer
from projectapp.serialisers import Video_Wall_PanelSerializer
from projectapp.serialisers import WorkstationSerializer

# Create your views here.
def index(request):
    return HttpResponse("This page can be used to test app functionality")

class Lights_GroupList(APIView):
    def get(self, request):
        Light_Groups = Light_Group.objects.all()
        serializer= Light_GroupSerializer(Light_Groups, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

class LightsList(APIView):
    def get(self, request):
        Lights1 = Light.objects.all()
        serializer= LightSerializer(Lights1, many=True)
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
        Workstations1 = Workstation.objects.all()
        serializer= WorkstationSerializer(Workstations1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

