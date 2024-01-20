from django.contrib import admin
from .models import Category, Department, Employee, Research, Works


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title', 'context']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    list_filter = ['fullname']
    search_fields = ['fullname', 'position']


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['context']


admin.site.register(Works)
