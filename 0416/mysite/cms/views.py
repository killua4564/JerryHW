from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def index(request):
	restaurant_list = Restaurant.objects.all()
	food_list = [Food.objects.filter(restaurant=restaurant) for restaurant in restaurant_list]
	return render(request, 'index.html', {'restaurant_zip': zip(restaurant_list, food_list)})

def person(request):
	people = Person.objects.all()
	return render(request, 'person.html', {'people': people})
