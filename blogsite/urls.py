"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views


urlpatterns = [
path('admin/', admin.site.urls),
path('', include('blog.urls')),  # Optional: make blog the home page
path('blog/', include('blog.urls', namespace='blog')),
path('accounts/login/', views.LoginView.as_view(), name='login'),
path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
path('accounts/password_change/', views.PasswordChangeView.as_view(),
name='accounts/password_change'),
path('accounts/password_change/done/', views.PasswordChangeDoneView.as_view(),
name='accounts/password_change_done'),
path('accounts/password_reset/', views.PasswordResetView.as_view(),
name='accounts/password_reset'),
path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(),
name='password_reset_done'),
path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
name='accounts/password_reset_confirm'),
path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(),
name='accounts/password_reset_complete'),
 
]



