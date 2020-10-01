from django.urls import path
from . import views

# Lsit of URL patterns
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]
