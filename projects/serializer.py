from rest_framework import serializers
from .models import Profile,Project,Rate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class RateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Rate
        fields = ('user','design','usability','content','score')

class ProjectSerializer(serializers.ModelSerializer):   
    rates = RateSerializer(many=True) 
    class Meta:
        model = Project
        fields = ('Title','Landingpage_img','Description','Livelink','rates')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'Profile_pic','User_bio','Address','projects')

    def create(self, validated_data):
        projects_data = validated_data.pop('projects')
        profile = Profile.objects.create(**validated_data)
        for project_data in projects_data:
            Project.objects.create(profile=profile, **project_data)
        return profile       

'''
data = {
    "user": {
        "username": "feven",
        "email": "feven.m.woldu@gmail.com"
    },
    "Profile_pic": "/media/photos/IMG_0208_gaZWYbv.JPG",
    "User_bio": "It's me Feven from Moringa School",
    "Address": "Nairobi,Kenya",
    "projects": [
        {
            "Title": "Movies",
            "Landingpage_img": "/media/photos/movies_nDFqfXB.png",
            "Description": "It's a website for displaying movies of different categories.Users can view them and give a review and comment on them.",
            "Livelink": "https://listofmoviestobewatched.herokuapp.com/"
        },
        {
            "Title": "Movies 2.0",
            "Landingpage_img": "/media/photos/movies_nDFqfXB.png",
            "Description": "Movies 2.0It's a website for displaying movies of different categories.Users can view them and give a review and comment on them.",
            "Livelink": "https://listofmoviestobewatched.herokuapp.com/"
        }
    ]
}


from projects.serializer import ProfileSerializer, ProjectSerializer
serializer = ProfileSerializer(instance=data)
serializer.is_valid()
'''        