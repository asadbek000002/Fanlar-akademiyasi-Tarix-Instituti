from django.shortcuts import render
from rest_framework import generics
from api.pagination import ResultsSetPagination
from library.models import Archive, AutoReferat, Category, Editorial, ElectronBook, Requirement, Source
from library.serializers import ArchiveSerializer, AutoReferatSerializer, Category_libSerializer, EditorialSerializer, ElektronBookSerializer, RequirementSerializer, SourceSerializer
from rest_framework import filters


class CategoryLibListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_libSerializer


class ArchiveListView(generics.ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer


class RequirementListView(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class EditorialListView(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class ElektronBookListView(generics.ListAPIView):
    queryset = ElectronBook.objects.all()
    serializer_class = ElektronBookSerializer
    pagination_class = ResultsSetPagination


class AutoReferatListView(generics.ListAPIView):
    queryset = AutoReferat.objects.all()
    serializer_class = AutoReferatSerializer
    pagination_class = ResultsSetPagination


class SourceListView(generics.ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = ResultsSetPagination

    

