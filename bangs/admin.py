from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Bang, TwitchUser


class MyUserAdmin(UserAdmin):
    list_display = ('email',)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Bang)
admin.site.register(TwitchUser)
