from api.pagination import ResultsSetPagination
from .models import Archive, AutoReferat, Category, Editorial, EditorialMany, ElectronBook, Requirement, Source
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class EditorialManySerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorialMany
        fields = '__all__'


class ElektronBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronBook
        fields = '__all__'
        pagination_class = ResultsSetPagination



class AutoReferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoReferat
        fields = '__all__'
        pagination_class = ResultsSetPagination


    
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
        pagination_class = ResultsSetPagination



