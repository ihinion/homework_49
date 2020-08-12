from django.db import models
from .validators import at_least_200, restricted_text_art


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description',
                                   validators=[restricted_text_art, ])
    detailed_desc = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Detailed description',
                                     validators=[at_least_200, restricted_text_art, ])
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT,
                               verbose_name='Status')
    types = models.ManyToManyField('webapp.Type', related_name='task_set', verbose_name='Types')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

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
