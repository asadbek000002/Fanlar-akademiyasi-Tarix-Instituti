from .models import Archive, AutoReferat, Category, Editorial, ElectronBook, Requirement, Source
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
        fields = '__all__'



class AutoReferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoReferat
        fields = '__all__'


    
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'



