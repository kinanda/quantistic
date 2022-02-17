from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dashboard.models import Project, SamplingProject

@login_required(login_url="/accounts/login/")
def dashboard_page(request):
    projects = Project.objects.filter(owner=request.user)
    sampling_projects = SamplingProject.objects.filter(owner=request.user)
    if "modal_message" in request.session:
        modal_message = request.session["modal_message"]
    context = {
        "user": request.user,
        "projects": projects,
        "sampling_projects": sampling_projects
    }
    return render(request, "dashboard/dashboard.html", context)
