from django.shortcuts import render
from rest_framework import viewsets, response, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from companyapi.serialiazers import (
    CompanySerializer, EmployeeSerializer, DepartmentSerializers
)
from companyapi.models import Company, Employee, Department


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @action(methods=['GET'], detail=True)
    def employee(self, request, pk):
        employee_list = Employee.objects.filter(companyId=pk)
        serializer = EmployeeSerializer(employee_list, many=True, context={'request': request})
        return response.Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentListView(
    generics.ListCreateAPIView
):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class DepartmentDetailView(APIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

    def get(self, request, pk):
        department = self.queryset.filter(pk=pk)
        return Response(self.serializer_class(department).data)



