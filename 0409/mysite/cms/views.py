from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def index(request):
	return HttpResponse('<h1>owo</h1>')
