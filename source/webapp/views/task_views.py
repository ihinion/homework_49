from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from webapp.models import Task, Project
from webapp.forms import ProjectTaskForm


class TaskView(DetailView):
    template_name = 'task/task.html'
    model = Task


class TaskUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'task/update.html'
    model = Task
    form_class = ProjectTaskForm

    def test_func(self):
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return self.request.user.has_perm('webapp.change_task') and \
            self.request.user in task.project.users.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'task/delete.html'
    model = Task

    def test_func(self):
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return self.request.user.has_perm('webapp.delete_task') and \
            self.request.user in task.project.users.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class ProjectTaskCreateView(UserPassesTestMixin, CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        types = form.cleaned_data.pop('types')
        task = form.save(commit=False)
        task.project = project
        task.save()
        task.types.set(types)
        return redirect('task_view', pk=task.pk)

    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return self.request.user.has_perm('webapp.add_task') and \
            self.request.user in project.users.all()
