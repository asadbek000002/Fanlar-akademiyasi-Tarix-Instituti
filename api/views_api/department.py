from django.shortcuts import get_object_or_404, render
from requests import Response
from rest_framework import generics
from department.models import  Department, Employee, Research, Poems
from department.serializers import  DepartmentSerializer, EmployeeSerializer, ResearchSerializer, \
    PoemsSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs['id']
        return Employee.objects.filter(department_id=department_id)

    


class ResearchListView(generics.ListAPIView):
    serializer_class = ResearchSerializer

    def get_queryset(self):
        department_id = self.kwargs['id']
        return Research.objects.filter(department_id=department_id)


class PoemsListView(generics.ListAPIView):
    queryset = Poems.objects.all()
    serializer_class = PoemsSerializer
