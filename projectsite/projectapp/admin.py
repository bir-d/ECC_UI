from django.contrib import admin
from projectapp.models import Lights
from projectapp.models import Lights_Group
from projectapp.models import Video_Wall_Panel
from projectapp.models import Video_Wall_Panel_Group
from projectapp.models import Workstations

# Register your models here.

admin.site.register(Lights_Group) 
admin.site.register(Lights)
admin.site.register(Video_Wall_Panel)
admin.site.register(Video_Wall_Panel_Group)
admin.site.register(Workstations)
