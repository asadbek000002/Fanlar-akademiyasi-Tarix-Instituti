from modeltranslation.translator import TranslationOptions, register
from .models import Category, Department, Employee, Research, Works

@register(Category)
class CategoryTranlationOption(TranslationOptions):
    fields = ('title', )


@register(Department)
class DepartmentTranlationOption(TranslationOptions):
    fields = ('title', 'context')


@register(Employee)
class EmployeeTranlationOption(TranslationOptions):
    fields = ('fullname', 'position', 'degree', 'bio' )


@register(Works)
class WorksTranlationOption(TranslationOptions):
    fields = ('works', )


@register(Research)
class ResearchTranlationOption(TranslationOptions):
    fields = ('context', )