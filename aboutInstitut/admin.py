from django.contrib import admin
from .models import Leadership, LeadershipImage


class LeadershipInline(admin.TabularInline):
    model = LeadershipImage
    extra = 0
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Image'
    verbose_name_plural = 'Images'
    list_display = ('image',)
    ordering = ('image',)


class LeadershipAdmin(admin.ModelAdmin):
    inlines = [LeadershipInline]
    list_display = ['position', 'full_name', 'degree', 'phone_number', 'email', 'reception_days', 'image']


admin.site.register(Leadership, LeadershipAdmin)
