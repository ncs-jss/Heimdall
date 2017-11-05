"""Heimdall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app import views as app_views
from attendence import views as att_views
from app import views as app_views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #====================== main app views ==========================================
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^$', app_views.index, name="index"),
    url(r'^home/$', app_views.home, name="home"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    

    #====================== attendance views ========================================
    url(r'^attendance/(?P<uid>\d+)$', att_views.AttendanceView.as_view()),
    url(r'^attendance/$', att_views.AttendanceView.as_view(), name="dailyAttendance"),



    #====================Django spaggeti View =======================================
    url(r'^plate/', include('django_spaghetti.urls')),


]

