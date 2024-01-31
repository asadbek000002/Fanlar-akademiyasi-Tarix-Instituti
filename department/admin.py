from django.contrib import admin
from .models import  Department, Employee, Research, Poems






@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title', 'context']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'created_time', 'updated_time']
    list_filter = ['fullname']
    search_fields = ['fullname', 'position']


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['context', 'created_time', 'updated_time']


@admin.register(Poems)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['works', 'created_time', 'updated_time']


