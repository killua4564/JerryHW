from django.shortcuts import render

from .models import *

def mother(request):
	content = ''
	if request.method == 'POST':
		content = request.POST.get('content')
		Mother.objects.create(content=content)
	return render(request, 'mother.html', {'content': content})
