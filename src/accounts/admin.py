# -*- coding: utf-8 -*-
from django.contrib import admin

from accounts.models import (UserType, UserProfile)


class UserProfileAdmin(admin.ModelAdmin):

    search_fields = ['user']
    list_display = ('user', 'user_type')
    model = UserProfile


admin.site.register(UserType)
admin.site.register(UserProfile, UserProfileAdmin)

