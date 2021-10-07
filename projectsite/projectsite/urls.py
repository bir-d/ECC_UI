"""projectsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('projectapp.urls')),

    #API Endpoints (GET,POST)
    # path('api/light_groups/', views.Lights_GroupView.as_view()),
    path('api/lights/', views.LightsView.as_view()),
    path('api/video_wall_groups/', views.Video_Wall_Panel_GroupView.as_view()),
    path('api/video_wall_panels/', views.Video_Wall_PanelView.as_view()),
    path('api/workstations/', views.WorkstationView.as_view()),
    path('api/displays/', views.DisplayView.as_view()),
    path('api/media/', views.MediaView.as_view()),
    path('api/preset/', views.PresetView.as_view()),

    #Indiviudal API Endpoints (GET,POST,PUT, Delete)
    # path('api/light_groups/<int:pk>', views.SingleLightGroupView.as_view()),
    path('api/lights/<int:pk>', views.SingleLightView.as_view()),
    path('api/video_wall_groups/<int:pk>', views.SingleVideoWallPanelGroupView.as_view()),
    path('api/video_wall_panels/<int:pk>', views.SingleVideoWallPanelView.as_view()),
    path('api/workstations/<int:pk>', views.SingleWorkstationView.as_view()),
    path('api/displays/<int:pk>', views.SingleDisplayView.as_view()),
    path('api/media/<int:pk>', views.SingleMediaView.as_view()),
    path('api/preset/<int:pk>', views.SinglePresetView.as_view()),

]
