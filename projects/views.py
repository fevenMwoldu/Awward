from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from . models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import photoForm, ProjectForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
        current_user = request.user    

        if not Profile.user_has_profile(current_user.id):
                return HttpResponseRedirect('profile')
        projects = Project.objects.all()
        return render(request, 'index.html',{"projects" : projects})


@login_required(login_url='/account/login/')
def add_project(request):
    print('add_project is called ....')
    current_user = request.user
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = Profile.objects.filter(user_id = current_user.id).first()
            project.save()
            print('Saved project {}'.format(project))
    
            return HttpResponseRedirect('/')
        
    return render(request, 'add_project.html', {"form": form})
