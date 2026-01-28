from django.db import models
import uuid
from .utils import *


class company(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, related_name="departments") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class employee(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField() 
    image = models.ImageField()
    document = models.TextField()
    designation = models.CharField(max_length=50)
    company = models.ForeignKey(company , on_delete=models.CASCADE,null=True,blank=True)    
    Department = models.ForeignKey(Department , on_delete=models.CASCADE, related_name="employees",null=True,blank=True) 
   

class Task(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(employee,on_delete=models.CASCADE,related_name='tasks',null=True,blank=True) 
    task_status = models.CharField(max_length=30,choices=TaskStatusEnum.choices(),default="pending",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    

    