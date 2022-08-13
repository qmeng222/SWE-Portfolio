from django.urls import path
from projects.views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
]
