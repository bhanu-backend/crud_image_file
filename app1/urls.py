
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name = 'home'),
    path('update/<int:id>/',views.update_pic,name = 'update'),
]