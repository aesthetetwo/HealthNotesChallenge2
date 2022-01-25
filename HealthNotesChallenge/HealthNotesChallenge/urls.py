"""HealthNotesChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from mywow.views import *
from django.conf.urls import url #include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # mywow/
    path('', mywow, name='mywow'),
    path('portal/', portal, name='portal'),
    url(r'^page1/$', page1, name='page1'),

    # conditions/
  
    url(r'^conditions/$', conditions, name='conditions'),

    # treaments/
    
    url(r'^treatments/$', treatments, name='treatments'),

]
