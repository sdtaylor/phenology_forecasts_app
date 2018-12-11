from django.shortcuts import render

from . import models

current_forecast_season = 2019

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
    
    #available_images = models.Forecasts.objects.filter(
    #        issue_date__forecast_season=current_forecast_season)
    
    image_metadata = {}
    image_metadata['available_species']=[s for s in available_species.values()]
    image_metadata['available_phenophase']=[p for p in available_phenophases.values()]
    #image_metadata['available_images']=[i for i in available_images.values()]
    image_metadata['available_issue_dates']=[d for d in available_issue_dates.values()]
    # make the issue date objects strings (ie. '2018-12-03') and set the default
    # to the most recent
    latest_issue_date=models.IssueDates.objects.latest('issue_date').issue_date
    for d in image_metadata['available_issue_dates']:
        if d['issue_date'] == latest_issue_date:
            d['default'] = 1
        else:
            d['default'] = 0
        d['issue_date'] = str(d['issue_date'])
    
    return image_metadata

def assign_selected(entries, field, selected_entry):
    for e in entries:
        if e[field]==selected_entry:
            e['default']=1
        else:
            e['default']=0
    return entries

def selected_image_metadata(issue_date, 
                            species, phenophase, as_json=True):
    """
    Make default image the one specified by a url instead of the one
    specified by the database.
    
    return dictionary
    """
    if issue_date=='latest':
        issue_date = str(models.IssueDates.objects.latest('issue_date').issue_date)

    select_image_info = models.Forecasts.objects.get(
                species__species=species, 
                phenophase__phenophase=phenophase, 
                issue_date__issue_date=issue_date)
    
    print('query select species')
    print(select_image_info)
    m = default_image_metatadata()
    m['available_issue_dates'] = assign_selected(m['available_issue_dates'], 
                                                field='issue_date',
                                                selected_entry = select_image_info.issue_date.issue_date)
    m['available_species'] = assign_selected(m['available_species'], 
                                                field='species',
                                                selected_entry = select_image_info.species.species)
    m['available_phenophase'] = assign_selected(m['available_phenophase'], 
                                                field='phenophase',
                                                selected_entry = select_image_info.phenophase.phenophase)
    return m
        
def Index(request, issue_date=None, 
          species=None, phenophase=None):
    selected_image_status=''
    url_entries = [issue_date, species, phenophase]
    # If a proprer URL
    if not None in url_entries:
        try:
            image_metadata = selected_image_metadata(issue_date=issue_date,
                                                     species=species,
                                                     phenophase=phenophase)
            selected_image_status='success'
        except:
            # nothing seems to be missing in url, but forecast couldn't be found
            selected_image_status='unavailable'
            image_metadata = default_image_metatadata()
    elif all([e is None for e in url_entries]):
        # no forecast specified in url
        selected_image_status='unspecified'
        image_metadata = default_image_metatadata()
    else:
        # Something maybe missing from url
        selected_image_status='unknown'
        image_metadata = default_image_metatadata()

    print(selected_image_status)
    image_metadata['selected_image_status']=selected_image_status
    return render(request, 'main/index.html', image_metadata)

def ImageMetadata(request,  forecast_season=None, issue_date=None, 
                  species=None, phenophase=None):
    
    pass