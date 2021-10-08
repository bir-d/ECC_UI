# from projectsite.projectapp.serialisers import Lights_GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_list_or_404
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from projectapp.models import Light_Group
from projectapp.models import Light
# from projectapp.models import Video_Wall_Panel_Group
from projectapp.models import Video_Wall
from projectapp.models import Workstation
from projectapp.models import Display
from projectapp.models import Media
from projectapp.models import Preset

# from projectapp.serialisers import Light_GroupSerializer
from projectapp.serialisers import LightSerializer
# from projectapp.serialisers import Video_Wall_Panel_GroupSerializer
from projectapp.serialisers import Video_WallSerializer
from projectapp.serialisers import WorkstationSerializer
from projectapp.serialisers import DisplaySerializer
from projectapp.serialisers import MediaSerializer
from projectapp.serialisers import PresetSerializer
# Create your views here.
def index(request):
    return HttpResponse("This page can be used to test app functionality")

#API Endpoint Views

# #Light Groups Endpoint
# class Lights_GroupView(ListCreateAPIView):
#     queryset = Light_Group.objects.all()
#     serializer_class = Light_GroupSerializer

#     def perform_create(self, serializer):
#         return serializer.save()

# class SingleLightGroupView(RetrieveUpdateDestroyAPIView):
#     queryset = Light_Group.objects.all()
#     serializer_class = Light_GroupSerializer

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

# #Video Wall Panel Groups Endpoint
# class Video_Wall_Panel_GroupView(ListCreateAPIView):
#     queryset = Video_Wall_Panel_Group.objects.all()
#     serializer_class = Video_Wall_Panel_GroupSerializer

#     def perform_create(self, serializer):
#         return serializer.save()

# #Individual Video Wall Groups Endpoint
# class SingleVideoWallPanelGroupView(RetrieveUpdateDestroyAPIView):
#     queryset = Video_Wall_Panel_Group.objects.all()
#     serializer_class = Video_Wall_Panel_GroupSerializer

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

# # GET request in Django API view for light groups
# class Lights_GroupList(APIView):
#     def get(self, request):
#         Light_Groups = Light_Group.objects.all()
#         serializer= Light_GroupSerializer(Light_Groups, many=True)
#         return Response({"Light Groups": serializer.data})

#  # POST request in Django API view for light groups       
#     def post(self, request):
#         light_group = request.data.get('light_group')

#         serializer = Light_GroupSerializer(data=light_group)
#         if serializer.is_valid(raise_exception=True):
#             light_group_saved = serializer.save()
#         return Response({"Success": "Light Group '{}' added successfully".format(light_group_saved.group_name)})

# # GET request in Django API view for lights
# class LightsList(APIView):
#     def get(self, request):
#         Lights1 = Light.objects.all()
#         serializer= LightSerializer(Lights1, many=True)
#         return Response({"Lights": serializer.data})

#  # POST request in Django API view for lights       
#     def post(self, request):
#         light = request.data.get('light')

#         serializer = LightSerializer(data=light)
#         if serializer.is_valid(raise_exception=True):
#             light_saved = serializer.save()
#         return Response({"Success": "Light '{}' added successfully".format(light_saved.name)})

# # GET request in Django API view for video wall panel groups     
# class Video_Wall_Panel_GroupList(APIView):
#     def get(self, request):
#         Video_Wall_Groups = Video_Wall_Panel_Group.objects.all()
#         serializer= Video_Wall_Panel_GroupSerializer(Video_Wall_Groups, many=True)
#         return Response({"Video Wall Panel Groups": serializer.data})

# # POST request in Django API view for video wall panel groups           
#     def post(self, request):
#         video_wall_panel_group = request.data.get('video_wall_panel_group')

#         serializer = Video_Wall_Panel_GroupSerializer(data=video_wall_panel_group)
#         if serializer.is_valid(raise_exception=True):
#             video_wall_panel_group_saved = serializer.save()
#         return Response({"Success": "Video Wall Panel Group '{}' added successfully".format(video_wall_panel_group_saved.id)})

# # GET request in Django API view for video wall panels
# class Video_Wall_PanelList(APIView):
#     def get(self, request):
#         Video_Wall_Panels = Video_Wall_Panel.objects.all()
#         serializer= Video_Wall_PanelSerializer(Video_Wall_Panels, many=True)
#         return Response({"Video Wall Panels": serializer.data})

# # POST request in Django API view for video wall panel groups     
#     def post(self, request):
#         video_wall_panel = request.data.get('video_wall_panel')

#         serializer = Video_Wall_PanelSerializer(data=video_wall_panel)
#         if serializer.is_valid(raise_exception=True):
#             video_wall_panel_saved = serializer.save()
#         return Response({"Success": "Video Wall Panel'{}' added successfully".format(video_wall_panel_saved.id)})

# # GET request in Django API view for workstations
# class WorkstationsList(APIView):
#     def get(self, request):
#         Workstations1 = Workstation.objects.all()
#         serializer= WorkstationSerializer(Workstations1, many=True)
#         return Response({"Workstations": serializer.data})

# # POST request in Django API view for workstations
#     def post(self, request):
#         workstation = request.data.get('workstation')

#         serializer = WorkstationSerializer(data=workstation)
#         if serializer.is_valid(raise_exception=True):
#             workstation_saved = serializer.save()
#         return Response({"Success": "Workstation '{}' added successfully".format(workstation_saved.id)})

