from django.shortcuts import render
from rest_framework import generics
from department.models import Category, Department, Employee, Research, Works
from department.serializers import CategorySerializer, DepartmentSerializer, EmployeeSerializer, ResearchSerializer, WorksSerializer

class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DepartmentListCreateView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListCreateView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ResearchListCreateView(generics.ListAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer


class WorksListCreateView(generics.ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer