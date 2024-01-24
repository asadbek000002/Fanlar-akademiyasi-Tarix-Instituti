from .models import Category, Department, Employee, Research, Works
from rest_framework import serializers

class Category_depSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['category', 'title', 'image', 'context']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['category', 'departmentemp', 'fullname', 'position', 'degree', 'email', 'bio','image']


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['category', 'departmentres', 'context']


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['category', 'employee', 'works']
