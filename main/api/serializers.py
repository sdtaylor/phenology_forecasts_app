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

# This one is used to list cause the StringRelatedField lets
# me see the actual entires for them instead of just primary keys
class ForecastsListSerializer(ModelSerializer):
    issue_date = StringRelatedField(many=False)
    species = StringRelatedField(many=False)
    phenophase = StringRelatedField(many=False)
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

# This is for create because I can't figure out how to create when
# StringRelatedField is used. But I have figured out how to create using 
# the primary keys. 
class ForecastsCreateSerializer(ModelSerializer):
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
