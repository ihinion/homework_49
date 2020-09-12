from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView, DetailView
from accounts.forms import MyUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Project


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        projects = Project.objects.filter(users__id=self.object.id)
        kwargs['projects'] = projects
        return super().get_context_data(**kwargs)