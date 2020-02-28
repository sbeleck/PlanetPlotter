from django.db import models
from reg_app.models import User

# Create your models here.

class Sector(models.Model):
    name = models.CharField(max_length=45, null=True)
    desc = models.TextField(null=True)
    public = models.BooleanField()
    map = models.ImageField(null=True)
    owned_by = models.ForeignKey(User, related_name="sectors", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class World(models.Model):
    name = models.CharField(max_length=45, null=True)
    desc = models.TextField(null=True)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    tag1 = models.CharField(max_length=45)
    tag2 = models.CharField(max_length=45)
    atmosphere = models.CharField(max_length=45)
    temperature = models.CharField(max_length=45)
    biosphere = models.CharField(max_length=45)
    population = models.CharField(max_length=45)
    gravity = models.CharField(max_length=45)
    techlevel = models.CharField(max_length=45)
    sector = models.ForeignKey(Sector, related_name="systems", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)