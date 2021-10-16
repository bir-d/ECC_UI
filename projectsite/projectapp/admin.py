from django.contrib import admin
from projectapp.models import Light
from projectapp.models import Video_Wall
from projectapp.models import Workstation
from projectapp.models import Display
from projectapp.models import Media
from projectapp.models import Preset

admin.site.register(Light)
admin.site.register(Video_Wall)
admin.site.register(Workstation)
admin.site.register(Display)
admin.site.register(Media)
admin.site.register(Preset)