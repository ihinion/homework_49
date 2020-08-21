from django.contrib import admin
from .models import Task, Status, Type, Project

# superuser
# login: admin
# password: admin
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)