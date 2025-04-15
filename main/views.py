from django.shortcuts import render
from team.models import Team

def index(request):

    return render(request, template_name='index.html')

def about(request):
    teams = Team.objects.all()
    return render(request, template_name='about.html', context={'teams': teams})