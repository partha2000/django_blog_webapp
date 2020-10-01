from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
{
	'author':'J.KJ rowling',
	'title':'Harry potter',
	'content':'childer book',
	'date_posted':'2007'
},
{
	"author":'Donald',
	'title':'Bill',
	'type':'Trump',
	'release':'18.10.1950'
}
]

def home(request):
	context = {
	'posts':posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	# return render(request, 'blog/about.html')
	return render(request, 'blog/about.html',{'title':'library'})