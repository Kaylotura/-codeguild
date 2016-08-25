"""DJANGO_APP_NAME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^GET/time', views.show_time_now, name='show_time_now'),
    url(r'^GET/(?P<lat>.+),(?P<lng>.+)/tz$', views.show_timezone,
        name='show_timezone'),
    url(r'^GET/(?P<lat>.+),(?P<lng>.+)/time$', views.show_time_for_timezone,
        name='show_time_for_timezone'),
    url(r'^GET/(?P<time>.+)/at/(?P<lat>.+),(?P<lng>.+)$',
        views.show_timezone_conversion, name='show_timezone_conversion')
]
