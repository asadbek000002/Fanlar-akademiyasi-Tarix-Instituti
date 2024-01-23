from django.contrib import admin
from .models import Archive, AutoReferat, Editorial, EditorialMany, ElectronBook, Requirement, Source, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']

@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']




class EditorialInline(admin.TabularInline):
    model =  EditorialMany


class EditorialAdmin(admin.ModelAdmin):
    inlines = [EditorialInline]
    list_display = ['fullname', 'degree', 'created_time', 'updated_time']

admin.site.register(Editorial, EditorialAdmin)




@admin.register(ElectronBook)
class ElektronBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']

@admin.register(AutoReferat)
class AutoReferatAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']

