from django.shortcuts import render
from .models import User
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def regi_view(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Registration Succesfully")
            messages.add_message(request, messages.INFO, 'Now You Can Login!!')
           
    else:
        fm = RegistrationForm()
    return render(request, 'app1/regi.html', {'form': fm})