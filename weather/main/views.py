# in this file I create all the views for the pages

from django.shortcuts import render, redirect
from django.http import HttpResponse
#import the scraper to get the data
from . import scraper

# Create home view.
def home(request):
    #If a location was searched redirect to the forecast page
    if request.method == 'POST':
        location = request.POST.get('location', False)
        if location:
            return redirect('/'+location)

    return render(request, 'main/home.html')
#Create forecast view
def forecast(request, location):
    #get the data from the scraper
    if location != 'favicon.ico':
        place, when, nature, current, precip, humid, wind = scraper.weather_scrape(location)
        if current and precip and humid and wind:
            context = {'place':place, 'when':when, 'nature':nature, 'current' : current, 'precip' : precip, 'humid':humid, 'wind':wind}
            #load the page with the data(context)
            return render(request, 'main/forecast.html', context)
    #if the scraper failed
        return HttpResponse('no data was found for the specific location, try with a big city near you')