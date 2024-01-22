from django.shortcuts import render
from rest_framework import generics
from library.models import Archive, AutoReferat, Category, Editorial, EditorialMany, ElectronBook, Requirement, Source
from library.serializers import ArchiveSerializer, AutoReferatSerializer, CategorySerializer, EditorialManySerializer, EditorialSerializer, ElektronBookSerializer, RequirementSerializer, SourceSerializer


class CategoryLibListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArchiveListCreateView(generics.ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer


class RequirementListCreateView(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class EditorialListCreateView(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class EditorialManyListCreateView(generics.ListAPIView):
    queryset = EditorialMany.objects.all()
    serializer_class = EditorialManySerializer


class ElektronBookListCreateView(generics.ListAPIView):
    queryset = ElectronBook.objects.all()
    serializer_class = ElektronBookSerializer


class AutoReferatListCreateView(generics.ListAPIView):
    queryset = AutoReferat.objects.all()
    serializer_class = AutoReferatSerializer


class SourceListCreateView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

