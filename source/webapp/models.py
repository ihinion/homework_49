from django.db import models

STATUS_CHOICES = [('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')]
TYPE_CHOICES = [('task', 'Task'), ('bug', 'Bug'), ('enhancement', 'Enhancement')]


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description')
    detailed_desc = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Detailed description')
    status = models.ForeignKey('webapp.Status', related_name='status_set', on_delete=models.PROTECT,
                               verbose_name='Status')
    type = models.ForeignKey('webapp.Type', related_name='status_set', on_delete=models.PROTECT,
                             verbose_name='Type')
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
