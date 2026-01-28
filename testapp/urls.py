from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [

    path('companies/', companyAPIView.as_view(), name='company-list-create'),
    path('companies/<str:pk>/', companyupdateAPIView.as_view(), name='company-update-delete'),

    path('Department/', DepartmentAPIView.as_view(), name='Department-list-create'),
    path('Department/<str:pk>/', DepartmentupdateAPIView.as_view(), name='Department-update-delete'),
  
    path('employee/', employeeAPIView.as_view(), name='employee-list-create'),
    path('employee/<str:pk>/', employeeupdateAPIView.as_view(), name='employee-update-delete'),

    path('Task/', TaskAPIView.as_view(), name='Task-list-create'),
    path('Task/<str:pk>/', TaskupdateAPIView.as_view(), name='Task-update-delete'),


    path('taskfilter/<str:task_status>/', TaskFilterAPIView.as_view()),
    path("employees/search/", EmployeeSearchAPIView.as_view()),


] 