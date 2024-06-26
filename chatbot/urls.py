from django.urls import path

from . import views

app_name = "chatbot"

urlpatterns = [
    path(
        "projects/create/",
        views.create_project_page,
        name="create_project_page",
    ),
    path(
        "projects/<str:project_id>/",
        views.view_project_page,
        name="view_project_page",
    ),
    path(
        "projects/<str:project_id>/edit",
        views.edit_project_page,
        name="edit_project_page",
    ),
    path(
        "projects/<str:project_id>/delete",
        views.delete_project_page,
        name="delete_project_page",
    ),
    path(
        "sampling-projects/create/",
        views.create_sampling_project_page,
        name="create_sampling_project_page",
    ),
    path(
        "sampling-projects/<str:project_id>/",
        views.view_sampling_project_page,
        name="view_sampling_project_page",
    ),
    path(
        "sampling-projects/<str:project_id>/edit",
        views.edit_sampling_project_page,
        name="edit_sampling_project_page",
    ),
    path(
        "sampling-projects/<str:project_id>/delete",
        views.delete_sampling_project_page,
        name="delete_sampling_project_page",
    ),
    path(
        "perasmian/",
        views.perasmian_page,
        name="perasmian_page",
    )
]
