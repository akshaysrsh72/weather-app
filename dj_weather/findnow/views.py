from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
def index_fn(request):
    #newurl='http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid=8e9916271649c4f4b299645781f95cd9'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8e9916271649c4f4b299645781f95cd9'
    if request.method=='POST':
        city=request.POST['city']
        #count=5
        r=requests.get(url.format(city)).json()
        result={
            'city': city,
            'temp':r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'humidity':r['main']['humidity']

        }
        context={'city_weather': result}
        print(context)
        print(json.dumps(r, indent=4))
    else:
        context={}
    return render(request, "index.html",context)





# Create your views here.
