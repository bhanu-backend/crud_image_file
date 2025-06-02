from django.shortcuts import render,redirect
from .models import AppUser
from django.http import HttpResponseRedirect

def home(request):
    if request.method == "POST":
         print(request.POST)
         print(request.FILES)
         name = request.POST.get('name')
         email = request.POST.get('email')
         category = request.POST.get('category')
         image = request.FILES.get('image')
         instance = AppUser(name=name,email=email ,image = image,category = category)
         instance.save()
         return redirect('home')





    return render(request,'app1/index.html')
