# Generated by Django 3.1.2 on 2020-12-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_fieldschedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arrivalnote',
            options={'verbose_name_plural': 'Arival notes'},
        ),
        migrations.AlterModelOptions(
            name='fieldplace',
            options={'verbose_name_plural': 'Field place'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='hours',
            field=models.PositiveIntegerField(default=0),
        ),
    ]