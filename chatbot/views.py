from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from chatbot.models import Flowchart
from dashboard.models import Project
from dashboard.forms import ProjectForm
from chatbot.descs import Description

@login_required(login_url="/accounts/login/")
def create_project_page(request):
    if request.method == 'POST':
        message = ""
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            if project_name == '':
                project_name = 'Untitled Project'
            project_path = form.cleaned_data['project_path']
            project_flowchart = Flowchart.objects.filter(path=project_path).first()
            project = Project.objects.create(
                name=project_name,
                owner=request.user,
                path=project_path,
                flowchart=project_flowchart,
            )
            project.save()
            message = "Project saved."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
    form = ProjectForm()
    context = {
        "form": form,
        "desc": Description.desc,
    }
    return render(request, "chatbot/create.html", context)


def view_project_page(request, project_id):
    return redirect("/")


@login_required(login_url="/accounts/login/")
def edit_project_page(request, project_id):
    if request.method == 'POST':
        message = ""
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            if project_name == '':
                project_name = 'Untitled Project'
            project_path = form.cleaned_data['project_path']
            project_flowchart = Flowchart.objects.filter(path=project_path).first()
            Project.objects.filter(id=project_id).update(
                name=project_name,
                path=project_path,
                flowchart=project_flowchart
            )
            message = "Project saved."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
    project = Project.objects.get(id=project_id)
    form = ProjectForm(initial={
        'project_name': project.name,
        'project_path': project.path
    })
    context = {
        "form": form,
        "desc": Description.desc,
        "path": project.path
    }
    return render(request, "chatbot/edit.html", context)


@login_required(login_url="/accounts/login/")
def delete_project_page(request, project_id):
    message = ""
    try:
        project = Project.objects.get(pk=project_id)
        project.delete()
        message = "Project '{}' deleted.".format(project.name)
    except Project.DoesNotExist:
        message = "Project does not exist."
    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
