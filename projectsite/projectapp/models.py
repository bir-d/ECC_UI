from django.db import models
from django.db.models.base import Model

class Lights_Group(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    group_name = models.CharField(max_length=255)
    colour = models.PositiveIntegerField()
    brightness = models.PositiveIntegerField()
    group_on = models.BooleanField()
    selected = models.BooleanField()

class Lights(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    colour = models.PositiveIntegerField()
    brightness = models.PositiveIntegerField()
    light_on = models.BooleanField()
    selected = models.BooleanField()
    group_id = models.ForeignKey(Lights_Group, on_delete=models.CASCADE)

class Video_Wall_Panel_Group(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    group_on = models.BooleanField()

class Video_Wall_Panel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    panel_on = models.BooleanField()
    video_wall_panel_group_id = models.ForeignKey(Video_Wall_Panel_Group, on_delete=models.CASCADE)

class Workstations(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    station_on = models.BooleanField()