from django.shortcuts import render

from . import models

current_forecast_season = 2018

# The json metadata file for the default index.html
def default_image_metatadata():
    """
    Metadata for the current default forecast of the website.
    
    returns dictionary
    """
    available_issue_dates = models.IssueDates.objects.filter(
            forecast_season=current_forecast_season)
    
    available_species = models.Speciess.objects.all()
    
    available_phenophases = models.Phenophases.objects.all()
    
    available_images = models.Forecasts.objects.filter(
            issue_date__forecast_season=current_forecast_season)
    
    image_metadata = {}
    image_metadata['available_issue_dates']=[d for d in available_issue_dates.values()]
    image_metadata['available_species']=[s for s in available_species.values()]
    image_metadata['available_phenophase']=[p for p in available_phenophases.values()]
    image_metadata['available_images']=[i for i in available_images.values()]
    
    return image_metadata

def assign_default(entries, field, field_default):
    for e in entries:
        if e[field]==field_default:
            e['default']=1
        else:
            e['default']=0
    return entries

def selected_image_metadata(forecast_season, issue_date, 
                            species, phenophase, as_json=True):
    """
    Make default image the one specified by a url instead of the one
    specified by the database.
    
    return dictionary
    """
    select_image_info = models.Forecasts.objects.get(
                species__species=species, 
                phenophase__phenophase=phenophase, 
                issue_date__issue_date=issue_date, 
                issue_date__forecast_season=forecast_season).__dict__
    
    m = default_image_metatadata()
    m['available_issue_dates'] = assign_default(m['available_issue_dates'], 
                                                field='issue_date',
                                                field_default = select_image_info.issue_date.issue_date)
    m['available_species'] = assign_default(m['available_species'], 
                                                field='speices',
                                                field_default = select_image_info.species.species)
    m['available_issue_phenophase'] = assign_default(m['available_phenophase'], 
                                                field='phenophase',
                                                field_default = select_image_info.phenophase.phenophase)
    return m
        
def Index(request, forecast_season=None, issue_date=None, 
          species=None, phenophase=None):
    selected_image_status=''
    url_entries = [forecast_season, issue_date, species, phenophase]
    # If a proprer URL
    if not None in url_entries:
        try:
            image_metadata = selected_image_metadata(forecast_season=forecast_season,
                                                        issue_date=issue_date,
                                                        species=species,
                                                        phenophase=phenophase)
        except:
            # nothing seems to be missing in url, but forecast couldn't be found
            selected_image_status='unavailable'
            image_metadata = default_image_metatadata()
    elif any([e is None for e in url_entries]):
        # Something maybe missing from url
        selected_image_status='unknown'
        image_metadata = default_image_metatadata()
    else:
        # no forecast specified in url
        image_metadata = default_image_metatadata()

    print(image_metadata)
    image_metadata['selected_image_status']=selected_image_status
    return render(request, 'main/index.html', image_metadata)

def ImageMetadata(request,  forecast_season, issue_date, species, phenophase):
    pass