# Generated by Django 2.2 on 2020-08-08 11:41

from django.db import migrations


def transfer_types(apps, schema_editor):
    Task = apps.get_model('webapp.Task')
    for task in Task.objects.all():
        task.types.add(task.type)


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_task_types'),

    ]

    operations = [
        migrations.RunPython(transfer_types)
    ]
