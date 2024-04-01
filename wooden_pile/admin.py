from django.contrib import admin
from .models import MainCategory, Tools, Modules, Question

# Register your models here.
@admin.register(MainCategory)
class AdminMainCategory(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tools)
class AdminTools(admin.ModelAdmin):
    list_display = ('id', 'title', 'origin')


@admin.register(Modules)
class AdminModules(admin.ModelAdmin):
    list_display = ('id', 'title', 'origin')


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ('question', 'responsive', 'proficiency', 'sort', 'set_time', 'res_mode', 'create_time')

