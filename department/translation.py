from modeltranslation.translator import TranslationOptions, register
from .models import Department, Employee, Research, Poems


class DepartmentTranlationOption(TranslationOptions):
    fields = ('title', 'context')


@register(Employee)
class EmployeeTranlationOption(TranslationOptions):
    fields = ('fullname', 'position', 'degree', 'bio')


@register(Poems)
class WorksTranlationOption(TranslationOptions):
    fields = ('works',)


@register(Research)
class ResearchTranlationOption(TranslationOptions):
    fields = ('context',)
