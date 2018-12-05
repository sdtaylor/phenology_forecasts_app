from rest_framework.serializers import ModelSerializer, StringRelatedField

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
    issue_date = StringRelatedField(many=False)
    species = StringRelatedField(many=False)
    phenophase = StringRelatedField(many=False)
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
