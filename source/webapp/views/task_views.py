from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm, ProjectTaskForm


class IndexView(ListView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(detailed_desc__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(DetailView):
    template_name = 'task/task.html'
    model = Task


# class TaskCreateView(PermissionRequiredMixin, CreateView):
#     template_name = 'task/create.html'
#     form_class = TaskForm
#     model = Task
#     permission_required = 'webapp.add_task'
#
#     # def has_permission(self):
#     #     task = self.get_object()
#     #     return super().has_permission() and self.request.user in task.project.users.all()
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.object.pk})


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
    template_name = 'task/create_from_project.html'
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
