from django.conf.urls import url

from .views import (
        SpeciessListAPIView, 
        SpeciessCreateAPIView,
        SpeciessUpdateAPIView,
        IssueDatesListAPIView,
        IssueDatesCreateAPIView,
        IssueDatesUpdateAPIView,
        ForecastsListAPIView,
        ForecastsCreateAPIView
        )
urlpatterns  = [
        url('species/list', SpeciessListAPIView.as_view(), name='species-list'),
        url('issuedates/list', IssueDatesListAPIView.as_view(), name='issuedates-list'),
        url('forecasts/list', ForecastsListAPIView.as_view(), name='forecasts-list'),
        url('species/create', SpeciessCreateAPIView.as_view(), name='species-create'),
        url('issuedates/create', IssueDatesCreateAPIView.as_view(), name='issuedates-create'),
        url('forecasts/create', ForecastsCreateAPIView.as_view(), name='forecasts-create'),
        url('species/update', SpeciessUpdateAPIView.as_view(), name='species-update'),
        url('issuedates/update', IssueDatesUpdateAPIView.as_view(), name='issuedates-update'),
  ]