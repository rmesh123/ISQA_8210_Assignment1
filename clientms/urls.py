from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('clients/', include('clients.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # Change Password
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
]