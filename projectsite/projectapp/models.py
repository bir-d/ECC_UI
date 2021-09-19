from django.db import models
from django.db.models.base import Model

class Lights_Group(models.Model):
    id = models.PositiveIntegerField(max_length=2)
    group_name = models.CharField(max_length=255)
    colour = models.PositiveIntegerField()
    brightness = models.PositiveIntegerField()
    group_on = models.BooleanField()
    selected = models.BooleanField()

class Lights(models.Model):
    light_id = models.PositiveIntegerField(max_length=100)
    name = models.CharField(max_length=255)
    colour = models.PositiveIntegerField()
    brightness = models.PositiveIntegerField()
    light_on = models.BooleanField()
    selected = models.BooleanField()
    group_id = models.ForeignKey(Lights_Group)

class Video_Wall_Panel_Group(models.Model):
    id = models.PositiveIntegerField(max_length=1)
    group_on = models.BooleanField()

class Video_Wall_Panel(models.Model):
    panel_id = models.PositiveIntegerField()
    panel_on = models.BooleanField()
    video_wall_panel_group_id = models.ForeignKey(Video_Wall_Panel_Group)

class Workstations(models.Model):
    workstation_id = models.PositiveIntegerField(max_length=1)
    station_on = models.BooleanField()