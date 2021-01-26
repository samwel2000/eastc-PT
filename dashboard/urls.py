from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('field-schedule/', views.fieldSchedulePage, name='field-schedule'),
    path('arrival-notes/', views.arrival_view, name='arrival-notes'),
    path('add-field-place/', views.addfieldplace_view, name='add-field-place'),
    path('field-place-details/', views.fieldplacedetails_view, name='field-place-details'),
    path('manage-users/', views.manageusers_view, name='manage-users'),
]
