
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
]
