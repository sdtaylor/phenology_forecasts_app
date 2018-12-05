from rest_framework.generics import (
        ListAPIView, 
        CreateAPIView,
        RetrieveUpdateAPIView
        )

from .serializers import SpeciessSerializer, ForecastsSerializer, IssueDatesSerializer
from main.models import Speciess, Forecasts, IssueDates

class SpeciessListAPIView(ListAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer

class SpeciessCreateAPIView(CreateAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer

class SpeciessUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Speciess.objects.all()
    serializer_class = SpeciessSerializer

class IssueDatesListAPIView(ListAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer

class IssueDatesCreateAPIView(CreateAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer

class IssueDatesUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IssueDates.objects.all()
    serializer_class = IssueDatesSerializer

class ForecastsListAPIView(ListAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer

class ForecastsCreateAPIView(CreateAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer