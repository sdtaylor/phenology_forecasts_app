from rest_framework.serializers import ModelSerializer

from main.models import Speciess, Forecasts, IssueDates

class SpeciessSerializer(ModelSerializer):
    class Meta:
        model = Speciess
        fields = [
                'species',
                'display_text',
                'default',
                ]
        
class ForecastsSerializer(ModelSerializer):
    class Meta:
        model = Forecasts
        fields = [
                'issue_date',
                'species',
                'phenophase',
                'image_filename',
                ]

class IssueDatesSerializer(ModelSerializer):
    class Meta:
        model = IssueDates
        fields = [
                'forecast_season',
                'issue_date',
                'display_text',
                'default',
                ]