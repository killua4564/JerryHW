from django.http import HttpResponse
from django.shortcuts import render

def search_form(request):
	return render(request, 'search_form.html')

def search(request):
	request.encoding = 'utf-8'
	message = 'What you fill in is: ' + request.GET.get('q')
	return HttpResponse(message)