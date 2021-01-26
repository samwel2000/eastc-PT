from .models import *
from datetime import datetime
def dashboard_renders(request):
    current_date = datetime.now()
    get_currentScheduleWeeks = FieldSchedule.objects.get(from_date__year=current_date.year) if FieldSchedule.objects.filter(from_date__year=current_date.year).exists() else None
    try:
        student = request.user
        fieldplaceCheck = FieldPlace.objects.filter(student=student, created_date__year=current_date.year)
        if fieldplaceCheck:
            fieldplace = FieldPlace.objects.get(student=student, created_date__year=current_date.year)
        else:
            fieldplace = None
    except:
        fieldplace = None

    return {
        'current_date':current_date,
        'fieldplace': fieldplace,
        'get_currentScheduleWeeks':get_currentScheduleWeeks
    }
