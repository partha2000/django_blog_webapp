from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Posts
# Create your views here.

# posts = [
# {
# 	'author':'J.K rowling',
# 	'title':'Harry potter',
# 	'content':'children book are not paying as told to her by the initial publishers',
# 	'date_posted':'2007'
# },
# {
# 	"author":'Donald Trump',
# 	'title':'Presidential Election',
# 	'content':'Donald trump to contest for the next term',
# 	'date_posted':'18.10.2020'
# }
# ]

def home(request):
	context = {
	'posts':Posts.objects.all()
	# 'posts': posts
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Posts
	template_name = 'blog/home.html'  ## Django will be looking for <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] ## Reverse chrono order


class PostDetailView(DetailView):
	model = Posts

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Posts
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
	model = Posts
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Posts
	success_url = ''
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
	

def about(request):
	# return render(request, 'blog/about.html')
	return render(request, 'blog/about.html',{'title':'library'})