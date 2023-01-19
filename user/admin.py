from django.contrib import admin
from user.models import User, Event


class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('name',)


admin.site.register(User, Users)


class Events(admin.ModelAdmin):
    list_display = ('id', 'place', 'name', 'date', 'managers', 'invite_number', 'event_budget')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'place',)
    list_per_page = 20


admin.site.register(Event, Events)
