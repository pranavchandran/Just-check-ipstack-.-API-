from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    # My code
    response = requests.get('http://api.ipstack.com/27.62.101.233?access_key=2fead77b0047c986e52385ef5678757c')
    geodata = response.json()
    print(geodata)  
    
    # response = requests.get('http://freegeoip.net/json/')
    # geodata = response.json()
    return render(request,'geo/home.html',{'geodata':geodata})
                # {'ip':geodata['ip'],
                # 'country':geodata['country_name']})


