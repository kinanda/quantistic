from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from chatbot.models import Flowchart, SamplingFlowchart
from dashboard.models import Project, SamplingProject
from dashboard.forms import ProjectForm, SamplingProjectForm
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

            project_progress = 0
            if project.flowchart.method.name.length >= 1:
                project_progress = 100
            elif project_path.length >= 3:
                project_progress = 75
            elif project_path.length >= 2:
                project_progress = 50
            elif project_path.length >= 1:
                project_progress = 25

            project = Project.objects.create(
                name=project_name,
                owner=request.user,
                path=project_path,
                flowchart=project_flowchart,
                progress=project_progress,
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

            project_progress = 0
            if project.flowchart.method.name.length >= 1:
                project_progress = 100
            elif project_path.length >= 3:
                project_progress = 75
            elif project_path.length >= 2:
                project_progress = 50
            elif project_path.length >= 1:
                project_progress = 25

            Project.objects.filter(id=project_id).update(
                name=project_name,
                path=project_path,
                flowchart=project_flowchart,
                progress=project_progress,
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


@login_required(login_url="/accounts/login/")
def create_sampling_project_page(request):
    if request.method == 'POST':
        message = ""
        form = SamplingProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            if project_name == '':
                project_name = 'Untitled Project'
            project_path = form.cleaned_data['project_path']
            project_flowchart = SamplingFlowchart.objects.filter(path=project_path).first()

            project_progress = 0
            if project.flowchart.method.name.length >= 1:
                project_progress = 100
            elif project_path.length >= 3:
                project_progress = 75
            elif project_path.length >= 2:
                project_progress = 50
            elif project_path.length >= 1:
                project_progress = 25

            project = SamplingProject.objects.create(
                name=project_name,
                owner=request.user,
                path=project_path,
                flowchart=project_flowchart,
                progress=project_progress,
            )
            project.save()
            message = "Project saved."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
    form = SamplingProjectForm()
    context = {
        "form": form,
        "desc": Description.desc,
    }
    return render(request, "chatbot/sampling_create.html", context)


def view_sampling_project_page(request, project_id):
    return redirect("/")


@login_required(login_url="/accounts/login/")
def edit_sampling_project_page(request, project_id):
    if request.method == 'POST':
        message = ""
        form = SamplingProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            if project_name == '':
                project_name = 'Untitled Project'
            project_path = form.cleaned_data['project_path']
            project_flowchart = SamplingFlowchart.objects.filter(path=project_path).first()

            project_progress = 0
            if project.flowchart.method.name.length >= 1:
                project_progress = 100
            elif project_path.length >= 3:
                project_progress = 75
            elif project_path.length >= 2:
                project_progress = 50
            elif project_path.length >= 1:
                project_progress = 25

            Project.objects.filter(id=project_id).update(
                name=project_name,
                path=project_path,
                flowchart=project_flowchart,
                progress=project_progress,
            )
            message = "Project saved."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
    project = SamplingProject.objects.get(id=project_id)
    form = SamplingProjectForm(initial={
        'project_name': project.name,
        'project_path': project.path
    })
    context = {
        "form": form,
        "desc": Description.desc,
        "path": project.path
    }
    return render(request, "chatbot/sampling_edit.html", context)


@login_required(login_url="/accounts/login/")
def delete_sampling_project_page(request, project_id):
    message = ""
    try:
        project = SamplingProject.objects.get(pk=project_id)
        project.delete()
        message = "Project '{}' deleted.".format(project.name)
    except SamplingProject.DoesNotExist:
        message = "Project does not exist."
    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
