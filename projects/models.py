from django.db import models

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length =30)
    Landingpage_img = models.ImageField(upload_to = 'photos/')
    Description = models.CharField(max_length =300)
    Livelink = models.CharField(max_length =100)
   
    

class Profile(models.Model):
    Profile_pic = models.ImageField(upload_to = 'photos/')
    User_bio = models.CharField(max_length =300)
    Project = models.ForeignKey(Project)
    Address = models.CharField(max_length =100)