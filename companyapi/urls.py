from rest_framework import routers
from .views import (CompanyViewSet, EmployeeViewSet,
                    DepartmentDetailView, DepartmentListView
                    )
from django.urls import path, include


apiroute = routers.DefaultRouter()

apiroute.register(r'company', CompanyViewSet)

apiroute.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('department/', DepartmentListView.as_view(), name='department-api'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-api'),
    path('', include(apiroute.urls))
]