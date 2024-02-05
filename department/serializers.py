from .models import Department, Employee, Research, Poems
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['title', 'image', 'context']


class PoemsSerializer(serializers.ModelSerializer):
    department_title = serializers.SerializerMethodField()

    class Meta:
        model = Poems
        fields = ['department', 'employee', 'works', 'department_title']

    def get_department_title(self, obj):
        return obj.department.title


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['department', 'fullname', 'position', 'degree', 'email', 'bio', 'image', 'file']


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['department', 'context']
