from rest_framework import serializers
from .models import *

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department 
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'      

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = '__all__' 




