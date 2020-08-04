from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, TemplateView
from .models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context


class TaskCreateView(View):
    def get(self, request):
        return render(request, 'create.html', {'form': TaskForm()})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', {'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            'description': task.description,
            'detailed_desc': task.detailed_desc,
            'status': task.status,
            'type': task.type
        })
        context['form'] = form
        context['task'] = task
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.filter(pk=pk).update(**form.cleaned_data)
            return redirect('task_view', pk=task.pk)
        else:
            return self.render_to_response({'form': form, 'task': task})