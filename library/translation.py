from modeltranslation.translator import TranslationOptions, register
from .models import Category, Archive, AutoReferat, Editorial, EditorialMany, ElectronBook, Requirement, Source

@register(Category)
class CategoryTranlationOption(TranslationOptions):
    fields = ('title', )


@register(Archive)
class ArchiveTranlationOption(TranslationOptions):
    fields = ('title', )
    

@register(Requirement)
class RequirementTranlationOption(TranslationOptions):
    fields = ('title', 'context')


@register(Editorial)
class EditorialTranlationOption(TranslationOptions):
    fields = ('fullname', 'degree', 'ish_joyi' )


@register(EditorialMany)
class EditorialTranlationOption(TranslationOptions):
    fields = ('fullname', 'degree', 'ish_joyi' )


@register(ElectronBook)
class ElectronBookTranlationOption(TranslationOptions):
    fields = ('title', )


@register(AutoReferat)
class AutoReferatTranlationOption(TranslationOptions):
    fields = ('title', )


@register(Source)
class SourceTranlationOption(TranslationOptions):
    fields = ('title', )