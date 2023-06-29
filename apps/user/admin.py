# coding=utf-8
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(User, UserAdmin)
