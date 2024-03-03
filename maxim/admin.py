from django.contrib import admin
from .models import Maxim

# Register your models here.
@admin.register(Maxim)
class MaximAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author', 'importance')
    list_filter = ('importance',)
    search_fields = ('quote', 'author')

