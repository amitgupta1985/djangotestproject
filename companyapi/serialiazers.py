"""
Create serializers
"""
from rest_framework import serializers
from .models import Company, Employee, Department


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'



