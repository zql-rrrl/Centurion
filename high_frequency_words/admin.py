from django.contrib import admin
from .models import Vocabulary

# Register your models here.
@admin.register(Vocabulary)
class AdminVocabulary(admin.ModelAdmin):
    list_display = ('sequence', 'word', 'part_of_speech', 'collins_star', 'meaning', 'root')
    list_filter = ('collins_star',)
