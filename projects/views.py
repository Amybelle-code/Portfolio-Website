from django.shortcuts import render
from projects.models import Project
"""
Here we create views for our model. Each view sends responses gotten from the Models 
back to the user. Also, class based views are used here.
"""

def project_index(request):
    """ 
    This function returns a collection of all objects in the table.
    The returned objects are stored in a dictionary and rendered with the
    projects_index.html template.
    """
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    """
    The project_detail function returns the data about the project whose id is passed.
    This query retrieves the project with primary key, pk, equal to that in the function argument.

    """
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
