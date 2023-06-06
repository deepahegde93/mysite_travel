from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img= models.ImageField(upload_to ='pics')
    designation=models.TextField()

    def __str__(self):
            return self.name

class People(models.Model):
    anam=models.CharField(max_length=250)
    aimg=models.ImageField(upload_to ="pics")
    ades=models.TextField()

    def __str__(self):
        return self.anam