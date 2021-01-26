# Generated by Django 3.1.2 on 2020-12-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_year', models.CharField(max_length=20)),
                ('weeks_number', models.PositiveIntegerField(default=0)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Field schedule',
            },
        ),
    ]