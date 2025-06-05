
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name = 'home'),
    path('update/<int:id>/',views.update_pic,name = 'update'),
    path('sign_up/',views.sign_up,name = 'signup'),
    path('log_in/',views.log_in,name = 'login'),
]