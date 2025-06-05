from django.shortcuts import render,redirect
from .models import AppUser,AuthenticateUser
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


def sign_up(request):
      if request.method == "POST":
         user_name = request.POST.get('username')
         password = request.POST.get('passwd')
         instance = AuthenticateUser(user_name=user_name,passwd=password)
         instance.save()
         return HttpResponseRedirect("/")
      return render(request,"app1/sign_up.html")

def log_in(request):
      if request.method == "POST":
            user_name = request.POST.get('username')
            password = request.POST.get('passwd')  
            user = AuthenticateUser.objects.filter(user_name=user_name).values()
            print(user)
            if user:
                  if user[0].get('passwd') == password :
                         name =user[0].get('user_name')
                         return render(request,"app1/profile.html",{'user':name})
                  else :
                        msg = "password incorrect "
                        return render(request,"app1/log_in.html",{'msg':msg}) 
            else:
               msg = "not a valid user "
               return render(request,"app1/log_in.html",{'msg':msg})



      return render(request,"app1/log_in.html")