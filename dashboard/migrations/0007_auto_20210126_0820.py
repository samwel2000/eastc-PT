# Generated by Django 3.1.2 on 2021-01-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20201223_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrivalnote',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fieldplace',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
