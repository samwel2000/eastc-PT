from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import *
from accounts.models import *
from .forms import *
from datetime import datetime


# Create your views here.
current_date = datetime.now()

@login_required
def index(request):
    current_date = datetime.now()
    get_students = Profile.objects.filter(role_name = 'student')
    get_fieldplace_details = FieldPlace.objects.filter(created_date__year=current_date.year)
    get_current_studentsWith_fieldplacement = [i.student for i in get_fieldplace_details]
    get_submitted_arrivalNote = ArrivalNote.objects.filter(created_date__year=current_date.year)
    get_submitted_arrivalNoteUsers = [i.student for i in get_submitted_arrivalNote]
    totalBos1_submitted = 0
    totalBos2_submitted = 0
    for submitted_arrivalNote in get_submitted_arrivalNote:
        if submitted_arrivalNote.student.profile.program == 'BOS1':
            totalBos1_submitted += 1
        elif submitted_arrivalNote.student.profile.program == 'BOS2':
            totalBos2_submitted += 1
    get_users_totals = Profile.objects.all().values('program').annotate(Sum('count'))
    get_currentAvailablePrograms = [i['program'] for i in get_users_totals]
    get_tasks = Task.objects.filter(created_date__year=current_date.year).order_by('week')
    content = {
        'page_title': 'Dashboard',
        'get_students': get_students,
        'field_place_details':get_fieldplace_details,
        'current_studentsWith_fieldplacement':get_current_studentsWith_fieldplacement,
        'users_totals':get_users_totals,
        'programs':get_currentAvailablePrograms,
        'submitted_arrivalNote': get_submitted_arrivalNoteUsers,
        'totalBos1_submitted':totalBos1_submitted,
        'totalBos2_submitted':totalBos2_submitted,
        'task_data':get_tasks,
        }
    template_name = 'dashboard/index.html'
    return render(request,template_name,content)


@login_required
def tasks_view(request):
    current_date = datetime.now()
    get_currentScheduleWeeks = FieldSchedule.objects.get(from_date__year=current_date.year) if FieldSchedule.objects.filter(from_date__year=current_date.year).exists() else None
    get_weeks = [i+1 for i in range(int(get_currentScheduleWeeks.weeks_number))] if get_currentScheduleWeeks else None
    get_days  = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    get_user_fromRequest = request.user
    get_user = User.objects.get(username=get_user_fromRequest)

    if request.method == 'POST':
        get_week = request.POST.get('week')
        get_day = request.POST.get('day')
        task_form = TaskForm(request.POST or None)
        if task_form.is_valid():
            instance = task_form.save(commit=False)
            instance.week = get_week[-1]
            instance.day = get_day
            instance.student = get_user
            instance.save()
            messages.success(request, f'Query Ok, Task and lesson learnt on {get_day.upper()} - {get_week.upper()} added succesifully')
            return redirect('dashboard:tasks')

    task_form = TaskForm()
    get_arrival_note = ArrivalNote.objects.get(student=get_user,created_date__year=current_date.year) if ArrivalNote.objects.filter(student=get_user,created_date__year=current_date.year).exists() else None
    get_tasks = list(Task.objects.filter(student=get_user, created_date__year=current_date.year).order_by('week'))

    get_totaltasksByweek= list(Task.objects.filter(student=get_user, created_date__year=current_date.year).values('week').annotate(Sum('const')))

    if get_weeks:
        for i in get_weeks:
            if i not in [task['week'] for task in get_totaltasksByweek]:
                dummy_count = {}
                dummy_count['week'] = i
                dummy_count['const__sum'] = 0
                get_totaltasksByweek.append(dummy_count)

    for task in get_totaltasksByweek:
        if task['const__sum'] < 5:
            get_daysByweek = Task.objects.filter(student=get_user,created_date__year=current_date.year,week=task['week']).values('day')
            get_daysByweek = [day['day'] for day in get_daysByweek]
            for day in get_days:
                dummy_task = {}
                dummy_task['week'] = task['week']
                if day not in get_daysByweek:
                    dummy_task['day'] = day
                    get_tasks.append(dummy_task)

    context = {
        'page_title': 'Field tasks',
        'form':task_form,
        'get_tasks':get_tasks,
        'arrival_note':get_arrival_note,
        'date':current_date,
        'scheduledWeeks':get_weeks,
        'days':get_days,
    }
    return render(request, 'dashboard/tasks.html', context)


@login_required
def arrival_view(request):
    current_date = datetime.now()
    get_currentScheduleWeeks = FieldSchedule.objects.get(from_date__year=current_date.year) if FieldSchedule.objects.filter(from_date__year=current_date.year).exists() else None
    if request.method == 'POST':
        form = ArrivalUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            messages.success(request, f'You have succesifully uploaded your arrival note')
            return redirect('dashboard:arrival-notes')

    form = ArrivalUploadForm()
    get_user_arrivalUpload = ArrivalNote.objects.get(student=request.user,created_date__year=current_date.year) if ArrivalNote.objects.filter(student=request.user,created_date__year=current_date.year).exists() else None
    context = {
        'page_title': 'Arrival notes',
        'form': form,
        'date':current_date,
        'currentSchedule':get_currentScheduleWeeks,
        'user_arrived':get_user_arrivalUpload,
    }
    return render(request, 'dashboard/arrival-notes.html', context)


@login_required
def addfieldplace_view(request):
    if request.method == 'POST':
        form = AddFieldPlaceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('dashboard:add-field-place')

    student = request.user
    current_date = datetime.now()
    fieldplaceCheck = FieldPlace.objects.filter(student=student,created_date__year=current_date.year)
    form = AddFieldPlaceForm()
    context = {
        'page_title': 'Add field place',
        'form': form,
        'fieldplaceCheck':fieldplaceCheck,
    }
    return render(request, 'dashboard/add-field-place.html', context)


@login_required
def fieldplacedetails_view(request):
    current_date = datetime.now()
    student = request.user
    get_users = User.objects.all()
    fieldplaceCheck = FieldPlace.objects.filter(student=student,created_date__year=current_date.year)
    if fieldplaceCheck:
        fieldplace = FieldPlace.objects.get(student=student, created_date__year=current_date.year)
    else:
        fieldplace = None
    context = {
        'page_title': 'Field place details',
        'fieldplace': fieldplace,
        'users':get_users
    }
    return render(request, 'dashboard/field-place-details.html', context)

@login_required
def manageusers_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, f'Query OK, user created succesifully')
            return redirect('dashboard:manage-users')
    user_form = UserRegistrationForm()
    profile_form = ProfileForm()
    get_users = User.objects.all().order_by("-id")
    page_title = "Manage users"
    template_name = 'dashboard/manageUsers.html'
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'users':get_users,
        'page_title':page_title
    }
    return render(request, template_name, context)

@login_required
def fieldSchedulePage(request):
    current_date = datetime.now()
    get_all_fieldSchedules = FieldSchedule.objects.all()
    get_specificSchedule = FieldSchedule.objects.get(from_date__year=current_date.year) if FieldSchedule.objects.filter(from_date__year=current_date.year).exists() else None
    if request.method == 'POST' and "add_button" in request.POST:
        schedule_form = FieldScheduleForm(request.POST or None)
        academic_year = schedule_form.data['study_year']
        if schedule_form.is_valid():
            schedule_form.save()
            # messages.success(request, f'Query Ok, Field schedule for academic year {academic_year} added succesifully')
            return redirect('dashboard:field-schedule')
    if request.method == 'POST' and "edit_button" in request.POST:
        schedule_form = FieldScheduleForm(request.POST, instance=get_specificSchedule)
        academic_year = schedule_form.data['study_year']
        if schedule_form.is_valid():
            schedule_form.save()
            messages.success(request, f'Query OK, Field schedule for academic year {academic_year} updated succesifully')
            return redirect('dashboard:field-schedule')
    schedule_form = FieldScheduleForm()
    if get_specificSchedule:
        schedule_form = FieldScheduleForm(instance=get_specificSchedule)
    template_name = 'dashboard/fieldSchedule.html'
    context = {
        'page_title':"Field Schedule",
        'form':schedule_form,
        'date':current_date,
        'specificSchedule':get_specificSchedule,
        'all_fieldSchedules':get_all_fieldSchedules
    }
    return render(request, template_name, context)
