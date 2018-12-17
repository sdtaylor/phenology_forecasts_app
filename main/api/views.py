from rest_framework.generics import (
        ListAPIView, 
        CreateAPIView,
        RetrieveUpdateAPIView,
        RetrieveAPIView
        )

# Default is set to IsAuthenticated
from rest_framework.permissions import (
        AllowAny
        )

from rest_framework.exceptions import NotFound

from .serializers import (
        SpeciessSerializer, 
        PhenophaseSerializer, 
        ForecastsSerializer, 
        IssueDatesSerializer
        )

from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from main.models import Speciess, Phenophases, Forecasts, IssueDates

class SpeciessListAPIView(ListAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer
    permission_classes = [AllowAny]

class SpeciessCreateAPIView(CreateAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer

class SpeciessUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer
    lookup_field='species'

class PhenophasesListAPIView(ListAPIView):
    queryset = Phenophases.objects.all()
    serializer_class = PhenophaseSerializer
    permission_classes = [AllowAny]

class IssueDatesListAPIView(ListAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer
    permission_classes = [AllowAny]

class IssueDatesCreateAPIView(CreateAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer

class IssueDatesUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer
    lookup_field = 'issue_date'

class ForecastsListAPIView(ListAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer
    permission_classes = [AllowAny]

class SpeciesForecastsDetailAPIView(ListAPIView):
    """
    Note this takes a get query. ie:
        '/api/forecasts/detail/?issue_date=2018-12-14&species=acer_rubrum
    """
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('issue_date', 'species')

class ForecastsCreateAPIView(CreateAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer

def InvalidAPICallView(request):
    raise NotFound()
