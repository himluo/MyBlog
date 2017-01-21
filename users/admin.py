from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MyUser


class EmployeeInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'myuser'


class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

