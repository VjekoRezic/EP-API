# Generated by Django 4.2 on 2023-05-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_center', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WO_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category name')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
            ],
        ),
        migrations.CreateModel(
            name='WO_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('start_time', models.DateTimeField(verbose_name='start')),
                ('due_time', models.DateTimeField(verbose_name='due time')),
                ('complete_time', models.DateTimeField(verbose_name='complete time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='Updated at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL, verbose_name='assignee')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_order.wo_category', verbose_name='order category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_order.wo_status', verbose_name='order status')),
                ('work_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_center.workcenter', verbose_name='work center')),
            ],
        ),
    ]