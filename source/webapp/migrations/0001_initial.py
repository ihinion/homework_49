# Generated by Django 2.2 on 2020-08-04 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')], default='new', max_length=15, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('task', 'Task'), ('bug', 'Bug'), ('enhancement', 'Enhancement')], default='task', max_length=15, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('detailed_desc', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Detailed description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_set', to='webapp.Status', verbose_name='Status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_set', to='webapp.Type', verbose_name='Status')),
            ],
        ),
    ]
