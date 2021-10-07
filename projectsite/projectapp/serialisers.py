from rest_framework import serializers
# from .models import Light_Group
from .models import Light
from .models import Video_Wall_Panel_Group
from .models import Video_Wall_Panel 
from .models import Workstation
from .models import Display
from .models import Media
from .models import Preset

# class Light_GroupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Light_Group
#         fields = '__all__'

class LightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Light
        fields = '__all__'

class Video_Wall_Panel_GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video_Wall_Panel_Group
        fields = '__all__'

class Video_Wall_PanelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video_Wall_Panel
        fields = '__all__'

class WorkstationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workstation
        fields = '__all__'

class DisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Display
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = '__all__'

class PresetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preset
        fields = '__all__'

