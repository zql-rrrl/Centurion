from django.contrib import admin
from .models import EveryDay

# Register your models here.
@admin.register(EveryDay)
class AdminEveryDay(admin.ModelAdmin):
    list_display = ('sort', 'habit', 'state', 'categorize')
    list_filter = ('state',)

