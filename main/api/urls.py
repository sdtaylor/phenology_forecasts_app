from django.conf.urls import url

from .views import (
        SpeciessListAPIView, 
        SpeciessCreateAPIView,
        SpeciessUpdateAPIView,
        PhenophasesListAPIView,
        IssueDatesListAPIView,
        IssueDatesCreateAPIView,
        IssueDatesUpdateAPIView,
        ForecastsListAPIView,
        ForecastsCreateAPIView,
        InvalidAPICallView
        )
urlpatterns  = [
        url('species/list', SpeciessListAPIView.as_view(), name='species-list'),
        url('issuedates/list', IssueDatesListAPIView.as_view(), name='issuedates-list'),
        url('forecasts/list', ForecastsListAPIView.as_view(), name='forecasts-list'),
        url('phenophases/list', PhenophasesListAPIView.as_view(), name='forecasts-list'),
        url('species/create', SpeciessCreateAPIView.as_view(), name='species-create'),
        url('issuedates/create', IssueDatesCreateAPIView.as_view(), name='issuedates-create'),
        url('forecasts/create', ForecastsCreateAPIView.as_view(), name='forecasts-create'),
        url(r'^species/update/(?P<species>\w+_\w+)/$', SpeciessUpdateAPIView.as_view(), name='species-update'),
        url(r'^issuedates/update/(?P<issue_date>\d{4}-\d{2}-\d{2})/$', IssueDatesUpdateAPIView.as_view(), name='issuedates-update'),
        url(r'.*', InvalidAPICallView, name='api-invalid'),
  ]
