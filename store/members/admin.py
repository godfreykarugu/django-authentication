from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)

# mix user info and profile info
class ProfileInline(admin.StackedInline):
    model=Profile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username","first_name","last_name","email"]
    inlines = [ProfileInline]

# unregister the old way
admin.site.unregister(User)

# re-register the new way

admin.site.register(User,UserAdmin)

