from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FieldSchedule(models.Model):
    study_year = models.CharField(max_length=20)
    weeks_number = models.PositiveIntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Field schedule'

    def __str__(self):
        return str(self.weeks_number)+"weeks "+str(self.from_date)+" "+str(self.to_date)

class Task(models.Model):
    """
    Field tasks model

    """
    week = models.PositiveIntegerField()
    const = models.PositiveIntegerField(default=1)
    day = models.CharField(max_length=50)
    task = models.TextField()
    lesson = models.TextField()
    hours = models.PositiveIntegerField()
    submission_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Tasks'
    def __str__(self):
        return str(self.student)+" - "+"week"+str(self.week)+" - "+self.day

class ArrivalNote(models.Model):
    pdf = models.FileField(upload_to='media/arrivalPDF/')
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Arival notes'
    def __str__(self):
        return str(self.student)

class FieldPlace(models.Model):
    company_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    supervisor_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Field place'
    def __str__(self):
        return str(self.student) +" - "+ self.company_name
