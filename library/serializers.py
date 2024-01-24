from .models import Archive, AutoReferat, Category, Editorial, ElectronBook, Requirement, Source
from rest_framework import serializers

class Category_libSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ['title', 'image', 'category_arch']


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['title', 'context', 'image', 'category_req']


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['fullname', 'degree', 'ish_joyi', 'image', 'category_edit']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        info = instance.editorial.all()

        if info:
            data['researchers'] = [{'fullname': researcher.fullname,
                                    'defree':researcher.degree,
                                    'ish_joyi':researcher.ish_joyi
                                    } for researcher in info]

        return data


class ElektronBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronBook
        fields = ['title', 'image']



class AutoReferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoReferat
        fields = ['title', 'image']


    
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['title', 'image']



