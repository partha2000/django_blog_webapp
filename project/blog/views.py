from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
{
	'author':'J.K rowling',
	'title':'Harry potter',
	'content':'children book are not paying as told to her by the initial publishers',
	'date_posted':'2007'
},
{
	"author":'Donald Trump',
	'title':'Presidential Election',
	'content':'Donald trump to contest for the next term',
	'date_posted':'18.10.2020'
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