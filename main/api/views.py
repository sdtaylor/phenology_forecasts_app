from rest_framework.generics import (
        ListAPIView, 
        CreateAPIView,
        RetrieveUpdateAPIView
        )

# Default is set to IsAuthenticated
from rest_framework.permissions import (
        AllowAny
        )

from .serializers import SpeciessSerializer, ForecastsSerializer, IssueDatesSerializer
from main.models import Speciess, Forecasts, IssueDates

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

class ForecastsListAPIView(ListAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer
    permission_classes = [AllowAny]

class ForecastsCreateAPIView(CreateAPIView):
    queryset = Forecasts.objects.all()
    serializer_class = ForecastsSerializer
