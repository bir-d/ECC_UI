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
# from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="ECC API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# schema_view = get_swagger_view(title='ECC API')

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('app/', include('projectapp.urls')),

    #API Endpoints (GET,POST)
    # path('api/light_groups/', views.Lights_GroupView.as_view()),
    path('api/lights/', views.LightsView.as_view()),
    # path('api/video_wall_groups/', views.Video_Wall_Panel_GroupView.as_view()),
    path('api/video_wall/', views.Video_WallView.as_view()),
    path('api/workstations/', views.WorkstationView.as_view()),
    path('api/displays/', views.DisplayView.as_view()),
    path('api/media/', views.MediaView.as_view()),
    path('api/preset/', views.PresetView.as_view()),

    #Indiviudal API Endpoints (GET,POST,PUT, Delete)
    # path('api/light_groups/<int:pk>', views.SingleLightGroupView.as_view()),
    path('api/lights/<int:pk>', views.SingleLightView.as_view()),
    # path('api/video_wall_groups/<int:pk>', views.SingleVideoWallPanelGroupView.as_view()),
    path('api/video_wall/<int:pk>', views.SingleVideoWallPanelView.as_view()),
    path('api/workstations/<int:pk>', views.SingleWorkstationView.as_view()),
    path('api/displays/<int:pk>', views.SingleDisplayView.as_view()),
    path('api/media/<int:pk>', views.SingleMediaView.as_view()),
    path('api/preset/<int:pk>', views.SinglePresetView.as_view()),

]
