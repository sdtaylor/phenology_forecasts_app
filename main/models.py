from django.db import models

# Create your models here.
class IssueDates(models.Model):
    forecast_season = models.IntegerField()
    issue_date = models.DateField()
    display_text = models.CharField(max_length=20)
    default = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('forecast_season','issue_date')

    def __str__(self):
        return str(self.issue_date)

class Speciess(models.Model):
    species = models.CharField(max_length=50, unique=True)
    display_text = models.CharField(max_length = 100)
    default = models.IntegerField(default=0)
    
    def __str__(self):
        return self.species

class Phenophases(models.Model):
    phenophase = models.IntegerField(unique=True)
    display_text = models.CharField(max_length = 20)
    default = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.phenophase)


class Forecasts(models.Model):
    issue_date = models.DateField()
    species    = models.CharField(max_length=50)
    phenophase = models.IntegerField()
    prediction_image=models.CharField(max_length=100)
    uncertainty_image=models.CharField(max_length=100)
    anomaly_image=models.CharField(max_length=100)

    class Meta:
        unique_together = ('issue_date','species','phenophase')
    
    def __str__(self):
        return '-'.join([str(self.issue_date), str(self.species), str(self.phenophase)])
