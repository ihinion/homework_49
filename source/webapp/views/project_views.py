from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import SearchForm, ProjectForm, UpdateProjectUsers


class IndexView(ListView):
    template_name = 'project/index.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.request.user.groups.filter(name__in=['Team Lead', 'Project Manager']):
            context['user_list_perm'] = True
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.groups.filter(name__in=['Team Lead', 'Project Manager']):
            context['groups'] = True
        return context


class ProjectCreateView(UserPassesTestMixin, CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project

    def test_func(self):
        return self.request.user.has_perm('webapp.add_project')

    def form_valid(self, form):
        users = User.objects.filter(pk=self.request.user.pk)
        project = form.save(commit=False)
        project.save()
        project.users.set(users)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'project/update.html'
    form_class = ProjectForm
    model = Project

    def test_func(self):
        return self.request.user.has_perm('webapp.change_project')

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'project/delete.html'
    model = Project
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_project')


class UpdateProjectUsers(UserPassesTestMixin, UpdateView):
    template_name = 'project/update_users.html'
    form_class = UpdateProjectUsers
    model = Project

    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return self.request.user in project.users.all() \
               and self.request.user.groups.filter(name__in=['Team Lead', 'Project Manager'])

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})