from django.contrib import admin
from .models import Root, Word, Family, Prefix, PrefixVocabulary, Suffix, SuffixVocabulary

# Register your models here.
@admin.register(Root)
class AdminRoot(admin.ModelAdmin):
    list_display = ('root', 'meaning', 'origin', 'frequency')
    list_filter = ('frequency',)


@admin.register(Word)
class AdminWord(admin.ModelAdmin):
    list_display = ('root', 'term', 'meaning')


@admin.register(Family)
class AdminMainCategory(admin.ModelAdmin):
    list_display = ('word', 'term', 'meaning')


@admin.register(Prefix)
class AdminPrefix(admin.ModelAdmin):
    list_display = ('prefix', 'meaning', 'frequency')


@admin.register(PrefixVocabulary)
class AdminPrefixVocabulary(admin.ModelAdmin):
    list_display = ('prefix', 'term', 'meaning')


@admin.register(Suffix)
class AdminSuffix(admin.ModelAdmin):
    list_display = ('suffix', 'meaning', 'frequency')


@admin.register(SuffixVocabulary)
class AdminSuffixVocabulary(admin.ModelAdmin):
    list_display = ('suffix', 'term', 'meaning')
