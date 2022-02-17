from django.contrib import admin

from .models import login_data


@admin.register(login_data)
class login_dataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    search_fields = ('name',)