from rest_framework.generics import ListAPIView
from about_institute.models import Leadership, OrganizationStructure, ArchitecturalLegalDocuments, \
    HistoryInstitute, News
from about_institute.serializers import LeadershipSerializer, OrganizationStructureSerializer, \
    ArchitecturalLegalDocumentsSerializer, HistoryInstituteSerializer, NewsSerializer


class LeadershipAPIView(ListAPIView):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer


class OrganizationStructureAPIView(ListAPIView):
    queryset = OrganizationStructure.objects.all()
    serializer_class = OrganizationStructureSerializer


class ArchitecturalLegalDocumentsAPIView(ListAPIView):
    queryset = ArchitecturalLegalDocuments.objects.all()
    serializer_class = ArchitecturalLegalDocumentsSerializer


class HistoryInstituteAPIView(ListAPIView):
    queryset = HistoryInstitute.objects.all()
    serializer_class = HistoryInstituteSerializer


class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
