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
    url(r'^light_groups/', views.Lights_GroupList.as_view()),
    url(r'^lights/', views.LightsList.as_view()),
    url(r'^video_wall_groups/', views.Video_Wall_Panel_GroupList.as_view()),
    url(r'^video_wall_panels/', views.Video_Wall_PanelList.as_view()),
    url(r'^workstations/', views.WorkstationsList.as_view()),
]
