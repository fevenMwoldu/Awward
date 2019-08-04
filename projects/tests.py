from django.test import TestCase
from .models import Project,Profile,Rate,User

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
           
        user = User.objects.create(username = 'feven')
    
        self.Biography= Profile(Profile_pic = '/home/feven/Pictures/Moringa_pics', User_bio ='This is my biography', Address = 'Nairobi',user = user)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Biography,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.Biography.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username = 'feven')
        self.Biography= Profile(Profile_pic = '/home/feven/Pictures/Moringa_pics', User_bio ='This is my biography', Address = 'Nairobi',user = user)
        self.Biography.save_profile()

        self.new_project= Project(Title = 'movies',Landingpage_img = '/home/feven/Pictures/Moringa_pics',Description = 'This is description',Livelink = 'https://blogproject20199.herokuapp.com/', Profile  = self.Biography)
        self.new_project.save()

        self.new_project.Profile.add(self.profiles)
        


    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()

class RateTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        user = User.objects.create(username = 'feven')
        self.Biography= Profile(Profile_pic = '/home/feven/Pictures/Moringa_pics', User_bio ='This is my biography', Address = 'Nairobi',user = user)
        self.Biography.save_profile()

        self.new_project= Project(Title = 'movies',Landingpage_img = '/home/feven/Pictures/Moringa_pics',Description = 'This is description',Livelink = 'https://blogproject20199.herokuapp.com/', Profile  = self.Biography)
        self.new_project.save()

        self.rate = Rate(Project = self.new_project, User = user, Design=8.0, Usability=8.0, Content=8.0, Score=8.0)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rate))

    # Testing Save Method
    def test_save_method(self):
        self.rate.save_rate()
        rates = Rate.objects.all()
        self.assertTrue(len(rates) > 0.0)

    def tearDown(self):
        Rate.objects.all().delete()
    

        
