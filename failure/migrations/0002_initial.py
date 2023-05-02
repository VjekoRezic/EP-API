# Generated by Django 4.2 on 2023-05-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('failure', '0001_initial'),
        ('work_center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='failure',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL, verbose_name='reported by'),
        ),
        migrations.AddField(
            model_name='failure',
            name='solved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solver', to=settings.AUTH_USER_MODEL, verbose_name='solved by'),
        ),
        migrations.AddField(
            model_name='failure',
            name='work_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_center.workcenter', verbose_name='work center'),
        ),
        migrations.AddField(
            model_name='failure',
            name='work_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work_order.workorder', verbose_name='work order'),
        ),
    ]
