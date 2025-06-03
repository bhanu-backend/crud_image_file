from django.shortcuts import render,redirect
from .models import AppUser
from django.http import HttpResponseRedirect
import os
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
         return HttpResponseRedirect('/')
    users = AppUser.objects.all()
    return render(request,'app1/index.html',{'users':users})


def update_pic(request , id):
      user =  AppUser.objects.get(pk = id)
      if os.path.isfile(user.image.path):
                os.remove(user.image.path)
      image = request.FILES.get('image')
      user.image = image
      user.save()
      return HttpResponseRedirect('/')
