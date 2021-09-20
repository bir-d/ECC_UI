from django.db import models
from django.db.models.base import Model
from django.core.validators import MaxValueValidator

class Light_Group(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    group_name = models.CharField(max_length=255)
    colour = models.CharField(max_length=6)
    brightness = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    group_on = models.BooleanField()
    selected = models.BooleanField()

class Light(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=6)
    brightness = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    light_on = models.BooleanField()
    selected = models.BooleanField()
    group_id = models.ForeignKey(Light_Group, on_delete=models.CASCADE)

class Video_Wall_Panel_Group(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    group_on = models.BooleanField()

class Video_Wall_Panel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    panel_on = models.BooleanField()
    video_wall_panel_group_id = models.ForeignKey(Video_Wall_Panel_Group, on_delete=models.CASCADE)

class Workstation(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    station_on = models.BooleanField()