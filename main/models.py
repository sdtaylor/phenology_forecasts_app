from django.db import models

# Create your models here.
class IssueDates(models.Model):
    forecast_season = models.IntegerField()
    issue_date = models.CharField(max_length=12)
    display_text = models.CharField(max_length=20)
    default = models.IntegerField(default=0)
    
    def __str__(self):
        return self.issue_date

class Speciess(models.Model):
    species = models.CharField(max_length=50)
    display_text = models.CharField(max_length = 100)
    default = models.IntegerField(default=0)
    
    def __str__(self):
        return self.species

class Phenophases(models.Model):
    phenophase = models.IntegerField()
    display_text = models.CharField(max_length = 20)
    default = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.phenophase)


class Forecasts(models.Model):
    issue_date = models.ForeignKey(IssueDates, on_delete=models.CASCADE)
    species    = models.ForeignKey(Speciess, on_delete=models.CASCADE)
    phenophase = models.ForeignKey(Phenophases, on_delete=models.CASCADE)
    image_filename=models.CharField(max_length=100)
    
    def __str__(self):
        return '-'.join([str(self.issue_date), str(self.species), str(self.phenophase)])