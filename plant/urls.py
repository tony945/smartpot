"""plant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from gui import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls, name='backend'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name='password_reset_complete'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('index/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('login_action/', views.login_action),
    path('register/', views.register, name='register'),
    path('register_action/', views.register_action),
    path('register_plant/', views.register_plant),
    path('register_plant/action/', views.register_plant_action),
    path('user_panel/', views.user_panel),
    path('user_panel/password/', views.user_panel_password),
    path('user_panel/email/', views.user_panel_email),
    path('user_panel/plantname/',views.user_panel_plantname),
    path('user_panel/reset/', views.user_panel_resetplant),
    path('realtime_panel/', views.realtime_panel, name='home'),
    path('realtime_panel/scoring/', views.scoring),
    path('realtime_panel/autowater/', views.autowater),
    path('realtime_panel/light/', views.light),
    path('realtime_panel/manualwater/', views.manualwater),
    path('realtime_data_refresh/', views.realtime_data_refresh),
    path('statistics_panel/', views.statistics_panel, name='statistic'),
    path('statistics_panel_shift/', views.statistics_panel_shift),
    path('logout/', views.logout),
]
