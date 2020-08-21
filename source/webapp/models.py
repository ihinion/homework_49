from django.db import models
from .validators import restricted_text_art, no_caps


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description',
                                   validators=[restricted_text_art, no_caps, ])
    detailed_desc = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Detailed description',
                                     validators=[restricted_text_art, no_caps, ])
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT,
                               verbose_name='Status')
    types = models.ManyToManyField('webapp.Type', related_name='task_set', verbose_name='Types')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.PROTECT,
                                verbose_name='Project')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return f'{self.pk}. {self.description}'


class Status(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(max_length=400, verbose_name='Description')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date', null=True, blank=True)

    def __str__(self):
        return self.name