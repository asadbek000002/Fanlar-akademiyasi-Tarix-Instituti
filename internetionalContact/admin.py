from django.contrib import admin
from .models import InternationalResearchers, InternationalResearchersExpert, \
                    InternationalProjects


class InternationalResearchersInline(admin.TabularInline):
    model = InternationalResearchersExpert
    fk_name = 'researchers'


@admin.register(InternationalResearchers)
class InternationalResearchersAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['title', 'image']
    inlines = [InternationalResearchersInline]


@admin.register(InternationalProjects)
class InternationalProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'partner_organization', 'funding_organization', 'done_undone_year',
                    'project_status', 'image']


