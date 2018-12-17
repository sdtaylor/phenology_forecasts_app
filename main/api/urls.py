from django.conf.urls import url

from .views import (
        SpeciessListAPIView, 
        SpeciessCreateAPIView,
        SpeciessUpdateAPIView,
        SpeciesForecastsDetailAPIView,
        PhenophasesListAPIView,
        IssueDatesListAPIView,
        IssueDatesCreateAPIView,
        IssueDatesUpdateAPIView,
        ForecastsListAPIView,
        ForecastsCreateAPIView,
        InvalidAPICallView
        )

issue_date_regex = r'(?P<issue_date>\d{4}-\d{2}-\d{2})'
species_regex = r'(?P<species>\w+_\w+)'
phenophase_regex = r'(?P<phenophase>\w+)'

urlpatterns  = [
        url('forecasts/list', ForecastsListAPIView.as_view(), name='forecasts-list'),
        url('forecasts/detail/', SpeciesForecastsDetailAPIView.as_view(), name='forecasts-list'),
        url('forecasts/create', ForecastsCreateAPIView.as_view(), name='forecasts-create'),
        url('issuedates/list', IssueDatesListAPIView.as_view(), name='issuedates-list'),
        url(r'^issuedates/update/'+issue_date_regex+r'/$', IssueDatesUpdateAPIView.as_view(), name='issuedates-update'),
        url('issuedates/create', IssueDatesCreateAPIView.as_view(), name='issuedates-create'),
        url('phenophases/list', PhenophasesListAPIView.as_view(), name='forecasts-list'),
        url('species/list', SpeciessListAPIView.as_view(), name='species-list'),
        url('species/create', SpeciessCreateAPIView.as_view(), name='species-create'),
        url(r'^species/update/'+species_regex+'/$', SpeciessUpdateAPIView.as_view(), name='species-update'),
        url(r'.*', InvalidAPICallView, name='api-invalid'),
  ]
