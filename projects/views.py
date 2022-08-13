from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls.base import reverse_lazy


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "create.html"
    fields = ["title", "description", "technology", "members", "image"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "detail.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
