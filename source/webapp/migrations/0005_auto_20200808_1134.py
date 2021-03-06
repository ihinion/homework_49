# Generated by Django 2.2 on 2020-08-08 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200808_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.Status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.Type', verbose_name='Type'),
        ),
    ]
