from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length =30)
    Landingpage_img = models.ImageField(upload_to = 'photos/')
    Description = models.CharField(max_length =300)
    Livelink = models.CharField(max_length =100)

    def __str__(self):
        return self.Title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_projectTitle(cls,search_term):
        projects = cls.objects.filter(Title__icontains=search_term)
        return projects
   
    

class Profile(models.Model):
    Profile_pic = models.ImageField(upload_to = 'photos/')
    User_bio = models.CharField(max_length =300)
    Project = models.ForeignKey(Project)
    Address = models.CharField(max_length =100)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.Address

    def save_profile(self):
        self.save()

    @classmethod
    def user_has_profile(cls, user_id):
        profiles = Profile.objects.filter(user_id=user_id)
        return len(profiles) > 0