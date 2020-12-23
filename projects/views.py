from django.shortcuts import render

#import Project class from models.py
from projects.models import Project

def project_index(request):
    # Django ORM query to select all objects in the Project table
    # A database query returns a collection of all objects that match the query, known as a Queryset.
    projects = Project.objects.all()

    # create a dictionary context. the dictionary only has one entry projects
    # context dictionary is used to send information to the template.
    # every function needs to have a context dictionary
    context = {
        "projects": projects
    }
    # context dictionary should be passed in render() in each view function
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project
    }
    return render(request, 'project_detail.html', context)