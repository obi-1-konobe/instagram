from django.contrib.auth.models import User

from accounts.models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'about_me', 'phone_number', 'gender']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
