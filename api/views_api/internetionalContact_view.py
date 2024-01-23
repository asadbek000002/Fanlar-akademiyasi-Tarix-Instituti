from rest_framework.generics import ListAPIView
from internetionalContact.models import PartnerOrganizations, InternationalProjects, InternationalResearchers
from internetionalContact.serializers import PartnerOrganizationsSerializer, InternationalProjectsSerializer, \
                                            InternationalResearchersSerializer


class PartnerOrganizationsAPIView(ListAPIView):
    queryset = PartnerOrganizations.objects.all()
    serializer_class = PartnerOrganizationsSerializer


class DoneInternationalProjectsAPIView(ListAPIView):
    queryset = InternationalProjects.objects.all()
    serializer_class = InternationalProjectsSerializer

    def get_queryset(self):
        return InternationalProjects.objects.filter(project_status='done')


class NotDoneInternationalProjectsAPIView(ListAPIView):
    queryset = InternationalProjects.objects.all()
    serializer_class = InternationalProjectsSerializer

    def get_queryset(self):
        return InternationalProjects.objects.filter(project_status='not_done')


class InternationalResearchersAPIView(ListAPIView):
    queryset = InternationalResearchers.objects.all()
    serializer_class = InternationalResearchersSerializer