"""phenology_forecast_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path

from . import views

issue_date_regex = r'(?P<issue_date>\d{4}-\d{2}-\d{2}|latest)'
species_regex = r'(?P<species>\w+_\w+)'
phenophase_regex = r'(?P<phenophase>\d{3}|\w{2,10})'

app_name = 'main'
urlpatterns = [
    path('', views.Index, name='index'),
    path('about', views.About, name='about'),
    re_path(r'^'+issue_date_regex+r'/'+species_regex+r'/'+phenophase_regex+r'/$', views.Index, name='index'),
    #path('image_metadata/', views.ImageMetadata, name='imagemetadata'),
    #path('image_metadata/<forecast_season>/<issue_date>/<species>/<phenophase>', views.ImageMetadata, name='imagemetadata')
]
