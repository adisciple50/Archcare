"""Archcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ArchForms import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^forms/weekly', views.weekly_progress_report),
    url(r'^forms/daily', views.daily_progress_report),
    url(r'^forms/user', views.add_service_user),
    url(r'^forms/staff', views.add_staff_member),
    url(r'^forms/house', views.add_house),
    url(r'^requests/weekly', views.specify_week),
    url(r'^reports/weekly', views.show_weeks),
    url(r'^requests/daily', views.specify_days),
    url(r'^reports/daily', views.show_days),
    url(r'^$', views.index, name='index'),
]
