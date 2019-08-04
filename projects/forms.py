from django import forms
from .models import Project,Profile,Rate

class photoForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['Profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['Project','user']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['project','user','score']
        