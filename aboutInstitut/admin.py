from django.contrib import admin
from .models import Leadership, LeadershipImage, \
                    OrganizationStructure, OrganizationStructureImage, \
                    HistoryInstitute, HistoryInstituteImage, \
                    ArchitecturalLegalDocuments, \
                    News, NewsImage


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
    fk_name = 'leadership_img'


class LeadershipAdmin(admin.ModelAdmin):
    inlines = [LeadershipInline]
    list_display = ['position', 'full_name', 'degree', 'phone_number', 'email', 'reception_days', 'image', 'created_time', 'updated_time']


admin.site.register(Leadership, LeadershipAdmin)


class OrganizationStructureInline(admin.TabularInline):
    model = OrganizationStructureImage
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
    fk_name = 'organization_structure_img'


class OrganizationStructureAdmin(admin.ModelAdmin):
    inlines = [OrganizationStructureInline]
    list_display = ['image', 'created_time', 'updated_time']


admin.site.register(OrganizationStructure, OrganizationStructureAdmin)


class HistoryInstituteInline(admin.TabularInline):
    model = HistoryInstituteImage
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
    fk_name = 'history_institute_img'


class HistoryInstituteAdmin(admin.ModelAdmin):
    inlines = [HistoryInstituteInline]
    list_display = ['title', 'contex', 'image', 'created_time', 'updated_time']


admin.site.register(HistoryInstitute, HistoryInstituteAdmin)


class NewsInline(admin.TabularInline):
    model = NewsImage
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
    fk_name = 'news_img'


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsInline]
    list_display = ['title', 'context', 'image', 'created_time', 'updated_time']


admin.site.register(News, NewsAdmin)


class ArchitecturalLegalDocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']


admin.site.register(ArchitecturalLegalDocuments, ArchitecturalLegalDocumentsAdmin)

