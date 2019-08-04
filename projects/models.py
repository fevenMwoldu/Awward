from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Profile_pic = models.ImageField(upload_to = 'photos/')
    User_bio = models.CharField(max_length =300)
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

class Project(models.Model):
    Title = models.CharField(max_length =30)
    Landingpage_img = models.ImageField(upload_to = 'photos/')
    Description = models.CharField(max_length =300)
    Livelink = models.CharField(max_length =100)
    Profile = models.ForeignKey(Profile)

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

class Rate(models.Model):
    Project = models.ForeignKey(Project)
    User = models.ForeignKey(User)
    Design = models.DecimalField(max_digits=2, decimal_places=1)
    Usability = models.DecimalField(max_digits=2, decimal_places=1)
    Content = models.DecimalField(max_digits=2, decimal_places=1)
    Score = models.DecimalField(max_digits=2, decimal_places=1)

    @classmethod
    def create(cls, project, user, design, usability, content):
        return Rate(
            Project = project,
            User = user,
            Design = design,
            Usability = usability,
            Content = content,
            Score = round((design + usability + content) / 3, 1)
        )

    def __str__(self):
        return 'Rate(Project:{self.Project}, User:{self.User}, Design:{self.Design}, Usability:{self.Usability}, Content:{self.Content}, Score:{self.Score})'.format(self=self)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

   
    

