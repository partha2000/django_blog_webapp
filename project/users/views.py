from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Username')
            messages.success(request,f'Account created for {username}!') ## Alert message
            return redirect('blog-home')  ## Redirect to home
    else:
        form = UserRegistrationForm()   ## Blank form if no data
    return render(request, 'users/register.html', {'form': form})
