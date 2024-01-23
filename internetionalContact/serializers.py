from rest_framework import serializers
from .models import PartnerOrganizations, InternationalProjects, InternationalResearchers


class PartnerOrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganizations
        fields = '__all__'


class InternationalProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalProjects
        fields = '__all__'


class InternationalResearchersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalResearchers
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        researchers = instance.researchers.all()

        if researchers:
            request = self.context.get('request')
            data['researchers'] = [{'fullname': researcher.full_name,
                                    'activity_institution': researcher.activity_institution,
                                    'year_of_visit': researcher.year_of_visit} for researcher in researchers]

        return data
