from django.shortcuts import render
from rest_framework import generics
from department.models import Category, Department, Employee, Research, Works
from department.serializers import Category_depSerializer, DepartmentSerializer, EmployeeSerializer, ResearchSerializer, \
    WorksSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_depSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ResearchListView(generics.ListAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer


class WorksListView(generics.ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
