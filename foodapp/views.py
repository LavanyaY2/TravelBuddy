from django.shortcuts import render
import requests


# Create your views here.


# For homepage
def home(request):
    return render(request, "home/home.html")


# For catalogue page
API_KEY = 'CZ2cLAcAqcaM-KBIujkN-jW0GO5euZRvYkXJCZ9iocyfT4JaDSCl_jD5h7KZymcx5aFjh3Xu_NzJFZj12QfG9M_Dg_xlBMaOIN0XhcXuUFORLJC8g0pt9MZvT8xRYnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

PARAMETERS = {'term': 'coffee', 'limit': 50, 'radius':10000, 'location':'Toronto', 'offset': 50}


def menu(request):

    businesses = ''
    
    food = request.GET.get('term')
    city= request.GET.get('location')
    
    if city and food:
        response = requests.get(url = ENDPOINT, params = {'term': food, 'limit': 50, 'radius':10000, 'location':city, 'offset': 50}, headers= HEADERS)
   
        business_data = response.json()

        businesses = business_data['businesses']
    
    elif city:
        response = requests.get(url = ENDPOINT, params = {'term': '', 'limit': 50, 'radius':10000, 'location':city, 'offset': 50}, headers= HEADERS)
   
        business_data = response.json()

        businesses = business_data['businesses']

   
    context = {
        'businesses': businesses
    }

    return render(request, 'menu/menu.html', context)



