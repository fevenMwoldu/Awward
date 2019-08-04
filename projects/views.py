from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from . models import Project,Profile,Rate
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProjectForm,RateForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import IsAdminOrReadOnly

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
            project.Profile = Profile.objects.filter(user_id = current_user.id).first()
            project.save()
            print('Saved project {}'.format(project))
    
            return HttpResponseRedirect('/')
        
    return render(request, 'add_project.html', {"form": form})

def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_projects = Project.search_by_projectTitle(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_rate(request):
    print('rate is called with method: {}'.format(request.method))
    current_user = request.user
    form = RateForm()
    
    if request.method == 'POST':
        print('POST: {}'.format(request.POST))
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():            
            rate = form.save(commit=False)
            rate.user = current_user
            rate.project = Project.objects.get(id=request.POST['project_id'])
            rate.score = round((rate.design + rate.usability + rate.content) / 3, 1)
            rate.save()
            print('Saved rate {}'.format(rate))
    
            return HttpResponseRedirect('/')

    project_id = request.POST['project_id'] if request.method == 'POST' else request.GET['project_id']
    
    return render(request, 'add_rate.html', {"form": form, "project_id": project_id})

class ProfileList(APIView):
    def get(self, request, format=None):
        context={'request': request}
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    permission_classes = (IsAdminOrReadOnly,)



class ProjectList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    

    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)



