from rest_framework import serializers
from .models import PartnerOrganizations, InternationalProjects, InternationalResearchers


class PartnerOrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganizations
        fields = ['id', 'title', 'image', 'context']


class InternationalProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalProjects
        fields = ['id', 'project_name', 'partner_organization', 'funding_organization',
                  'done_undone_year', 'project_status', 'image']


class InternationalResearchersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalResearchers
        fields = ['id', 'title', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        researchers = instance.researchers.all()

        if researchers:
            request = self.context.get('request')
            data['researchers'] = [{'fullname': researcher.full_name,
                                    'activity_institution': researcher.activity_institution,
                                    'year_of_visit': researcher.year_of_visit} for researcher in researchers]

        return data
