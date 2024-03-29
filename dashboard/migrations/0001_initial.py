# Generated by Django 3.1.2 on 2020-12-08 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('task', models.TextField()),
                ('lesson', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FieldPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('supervisor_name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('student', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArrivalNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='media/pdfs/')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
