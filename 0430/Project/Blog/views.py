from django.utils import timezone
from django.shortcuts import render

from .models import Post

def Mothers_Day(request):
	if request.method == 'POST':
		author = request.POST.get('author')
		title = request.POST.get('title')
		text = request.POST.get('text')
		post = Post()
		post.author = author
		post.title = title
		post.text = text
		post.save()
	return render(request, 'Mothers_Day.html')

def blog(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog.html', {'posts': posts}) 