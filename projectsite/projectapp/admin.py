from django.contrib import admin
from projectapp.models import Light
from projectapp.models import Light_Group
from projectapp.models import Video_Wall_Panel
from projectapp.models import Video_Wall_Panel_Group
from projectapp.models import Workstation

# Register your models here.

admin.site.register(Light_Group) 
admin.site.register(Light)
admin.site.register(Video_Wall_Panel)
admin.site.register(Video_Wall_Panel_Group)
admin.site.register(Workstation)
