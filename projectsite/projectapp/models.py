from django.db import models
from django.db.models.base import Model
from django.core.validators import MaxValueValidator

# class Light_Group(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     group_name = models.CharField(max_length=255)
#     colour = models.CharField(max_length=6)
#     brightness = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
#     group_on = models.BooleanField()
#     selected = models.BooleanField()

#     def __str__(self):
#         return self.group_name

class Light(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=20)
    brightness = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    light_on = models.BooleanField()
    selected = models.BooleanField()
    # group_id = models.ForeignKey(Light_Group, on_delete=models.CASCADE)

    #Function to display light name as placeholder on admin page
    def __str__(self):
        return self.name

class Video_Wall_Panel_Group(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    media = models.CharField(max_length=255, null=True)
    group_on = models.BooleanField()
    
    #Function to display video wall panel group id as placeholder on admin page
    def __str__(self):
        return self.id

class Video_Wall_Panel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    media = models.CharField(max_length=255, null=True)
    panel_on = models.BooleanField()
    video_wall_panel_group_id = models.ForeignKey(Video_Wall_Panel_Group, on_delete=models.CASCADE)
    
    #Function to display video wall panel id as placeholder on admin page
    def __str__(self):
        return self.id

class Workstation(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    workstation_name = models.CharField(max_length=255)
    station_on = models.BooleanField()
    media = models.CharField(max_length=255, null=True)

    #Function to display workstation name as placeholder on admin page
    def __str__(self):
        return self.workstation_name

class Display(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    display_name = models.CharField(max_length=255)
    display_on = models.BooleanField()
    media = models.CharField(max_length=255, null=True)
    
    #Function to display workstation name as placeholder on admin page
    def __str__(self):
        return self.display_name

