from rest_framework.serializers import ModelSerializer, StringRelatedField, ValidationError

from main.models import Speciess, Forecasts, IssueDates, Phenophases

class SpeciessSerializer(ModelSerializer):
    class Meta:
        model = Speciess
        fields = [
                'id',
                'species',
                'display_text',
                'default',
                ]

class IssueDatesSerializer(ModelSerializer):
    class Meta:
        model = IssueDates
        fields = [
                'id',
                'forecast_season',
                'issue_date',
                'display_text',
                'default',
                ]
        
class PhenophaseSerializer(ModelSerializer):
    class Meta:
        model = Phenophases
        fields = [
                'id',
                'phenophase',
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
                'prediction_image',
                'uncertainty_image',
                'anomaly_image',
                ]
