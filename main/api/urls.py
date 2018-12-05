from django.conf.urls import url

from .views import (
        SpeciessListAPIView, 
        SpeciessCreateAPIView, 
        IssueDatesListAPIView,
        IssueDatesCreateAPIView,
        ForecastsListAPIView,
        ForecastsCreateAPIView
        )
urlpatterns  = [
        url('species/list', SpeciessListAPIView.as_view(), name='list'),
        url('issuedates/list', IssueDatesListAPIView.as_view(), name='list'),
        url('forecasts/list', ForecastsListAPIView.as_view(), name='list'),
        url('species/create', SpeciessCreateAPIView.as_view(), name='list'),
        url('issuedates/create', IssueDatesCreateAPIView.as_view(), name='list'),
        url('forecasts/create', ForecastsCreateAPIView.as_view(), name='list'),
  ]