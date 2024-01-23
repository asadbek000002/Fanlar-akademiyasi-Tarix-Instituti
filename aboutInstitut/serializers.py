from rest_framework import serializers
from .models import Leadership, OrganizationStructure, ArchitecturalLegalDocuments, \
    HistoryInstitute, News


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.leadership_img.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data


class OrganizationStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationStructure
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.organization_structure_img.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data


class ArchitecturalLegalDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitecturalLegalDocuments
        fields = '__all__'


class HistoryInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryInstitute
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.history_institute_img.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.news_img.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
