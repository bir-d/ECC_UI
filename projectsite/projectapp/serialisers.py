from rest_framework import serializers
from .models import Lights_Group
from .models import Lights 
from .models import Video_Wall_Panel_Group
from .models import Video_Wall_Panel 
from .models import Workstations

class Lights_GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lights_Group
        fields = '__all__'

class LightsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lights
        fields = '__all__'

class Video_Wall_Panel_GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video_Wall_Panel_Group
        fields = '__all__'

class Video_Wall_PanelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video_Wall_Panel
        fields = '__all__'

class WorkstationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workstations
        fields = '__all__'
