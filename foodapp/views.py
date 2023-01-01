from django.shortcuts import render, redirect
import requests
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
API_KEY = 'CZ2cLAcAqcaM-KBIujkN-jW0GO5euZRvYkXJCZ9iocyfT4JaDSCl_jD5h7KZymcx5aFjh3Xu_NzJFZj12QfG9M_Dg_xlBMaOIN0XhcXuUFORLJC8g0pt9MZvT8xRYnYx'
ENDPOINT_RESTAURANTS = 'https://api.yelp.com/v3/businesses/search'
ENDPOINT_HOME = 'https://api.yelp.com/v3/events'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# For homepage
def home(request):
    events = ''
    destination = request.GET.get('destination')
    if destination:
        response = requests.get(url = ENDPOINT_HOME , params = {'sort_on': 'popularity', 'limit':50, 'location': destination, 'is_canceled': False}, headers= HEADERS)
        events_data = response.json()
        events = events_data['events']
    context = {
        'events': events
    }
    return render(request, "home/home.html", context)

# For catalogue page
# PARAMETERS = {'term': 'coffee', 'limit': 50, 'radius':10000, 'location':' ' , 'offset': 50}
def menu(request):
    businesses = ''
    food = request.GET.get('term')
    city= request.GET.get('location')
    if city and food:
        response = requests.get(url = ENDPOINT_RESTAURANTS , params = {'term': food, 'limit': 50, 'radius':10000, 'location':city, 'offset': 50}, headers= HEADERS)
        business_data = response.json()
        businesses = business_data['businesses']
    elif city:
        response = requests.get(url = ENDPOINT_RESTAURANTS , params = {'term': '', 'limit': 50, 'radius':10000, 'location':city, 'offset': 50}, headers= HEADERS)
        business_data = response.json()
        businesses = business_data['businesses']
    context = {
        'businesses': businesses
    }
    return render(request, 'menu/menu.html', context)

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful")
            return redirect("home/home.html")
        messages.error(request, "invalid")
    form = NewUserForm()
    return render(request, 'register/register.html', context = {"register":form})
