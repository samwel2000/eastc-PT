from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(ArrivalNote)
admin.site.register(FieldPlace)
admin.site.register(FieldSchedule)
