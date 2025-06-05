from django.contrib import admin
from .models import AppUser,AuthenticateUser

admin.site.register(AppUser)
admin.site.register(AuthenticateUser)
