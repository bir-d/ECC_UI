from django.db import models
from django.db.models.base import Model
from django.core.validators import MaxValueValidator

class Light(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=20)
    brightness = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    light_on = models.BooleanField()
    selected = models.BooleanField()

    #Function to display light name as placeholder on admin page
    def __str__(self):
        return self.name
    
    #Functions for testing
    def getname(self):
        return self.name

    def getcolour(self):
        return self.colour
    
    def getbrightness(self):
        return self.brightness
    
    def getlight_on(self):
        return self.light_on
    
    def getselected(self):
        return self.selected

class Video_Wall(models.Model):
    id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=255, null=True)
    media_type = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)
    wall_on = models.BooleanField()

    #Functions for testing
    def getmedia_name(self):
        return self.media_name

    def getmedia_type(self):
        return self.media_type

    def getsource(self):
        return self.source

    def getwall_on(self):
        return self.wall_on
   
class Workstation(models.Model):
    id = models.AutoField(primary_key=True)
    workstation_name = models.CharField(max_length=255)
    station_on = models.BooleanField()
    media_name = models.CharField(max_length=255, null=True)
    media_type = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)

    #Function to display workstation name as placeholder on admin page
    def __str__(self):
        return self.workstation_name

    #Functions for testing
    def getworkstation_name(self):
        return self.workstation_name

    def getstation_on(self):
        return self.station_on

    def getmedia_name(self):
        return self.media_name

    def getmedia_type(self):
        return self.media_type

    def getsource(self):
        return self.source


class Display(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=255)
    display_on = models.BooleanField()
    media_name = models.CharField(max_length=255, null=True)
    media_type = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)
    
    #Function to display workstation name as placeholder on admin page
    def __str__(self):
        return self.display_name

    #Functions for testing
    def getdisplay_name(self):
        return self.display_name

    def getdisplay_on(self):
        return self.display_on

    def getmedia_name(self):
        return self.media_name

    def getmedia_type(self):
        return self.media_type

    def gesource(self):
        return self.source



class Media(models.Model):
    id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=255, null=True)
    media_type = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)

    #Function to display media name as placeholder on admin page
    def __str__(self):
        return self.media_name

    #Functions for testing
    def getmedia_name(self):
        return self.media_name

    def getmedia_type(self):
        return self.media_type

    def getsource(self):
        return self.source

class Preset(models.Model):
    id = models.AutoField(primary_key=True)
    preset_name = models.CharField(max_length=255, null=True)
    lights = models.JSONField(null=True)
    video_Wall = models.JSONField(null=True)
    workstations = models.JSONField(null=True)
    displays = models.JSONField(null=True)

    #Function to display preset name as placeholder on admin page
    def __str__(self):
        return self.preset_name

    #Functions for testing
    def getpreset_name(self):
        return self.preset_name

    def getlights(self):
        return self.lights

    def getvideo_Wall(self):
        return self.video_Wall

    def getworkstations(self):
        return self.workstations

    def getdisplays(self):
        return self.displays
