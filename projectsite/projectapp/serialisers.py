from rest_framework import serializers
from .models import Light
from .models import Video_Wall
from .models import Workstation
from .models import Display
from .models import Media
from .models import Preset

#Serialiser for lights to get all fields from model for API
class LightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Light
        fields = '__all__'

#Serialiser for video wall to get all fields from model for API
class Video_WallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video_Wall
        fields = '__all__'

#Serialiser for workstations to get all fields from model for API
class WorkstationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workstation
        fields = '__all__'

#Serialiser for displays to get all fields from model for API
class DisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Display
        fields = '__all__'

#Serialiser for media to get all fields from model for API
class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = '__all__'

#Serialiser for presets to get all fields from model for API
class PresetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preset
        fields = '__all__'

