from django.shortcuts import render
from django.template import loader 
from .models import Project

def project_list(request):
    
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_list.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)
