from django.db import models

# Create your models here.



class Toilet(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField(null=True ,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name


class Room(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField(null=True ,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    toilet = models.ForeignKey(Toilet,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return  self.name
class Image(models.Model):
    name =  models.CharField(max_length=200)
    image=models.FileField()
    

    def __str__(self):
        return  self.name
