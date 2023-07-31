from django.contrib import admin

# Register your models here.

from .models import complaints, opinion


@admin.register(complaints)
class complaintsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(opinion)
class opinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'active')