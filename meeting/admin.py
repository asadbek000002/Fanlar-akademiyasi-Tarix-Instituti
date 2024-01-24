from django.contrib import admin
from .models import ConferencesCategory, Conferences, ConferencesImg


@admin.register(ConferencesCategory)
class ConferencesCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class ConferencesImgInline(admin.TabularInline):
    model = ConferencesImg
    fk_name = 'conferences_img'


@admin.register(Conferences)
class ConferencesAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'context']
    list_filter = ['category', 'title', 'context']
    inlines = [ConferencesImgInline]
