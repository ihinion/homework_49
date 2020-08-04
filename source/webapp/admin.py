from django.contrib import admin
from .models import Task, Status, Type

# superuser
# login: admin
# password: admin
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Type)
