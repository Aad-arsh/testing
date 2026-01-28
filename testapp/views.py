from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *
from elasticsearch import Elasticsearch

class companyAPIView(APIView):
    # GET (list)
    def get(self, request):
        items = company.objects.all()
        serializer = companySerializer(items, many=True) 
        return Response(serializer.data) 

    # POST (create)
    def post(self, request):
        serializer = companySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class companyupdateAPIView(APIView):
    def put(self, request, pk):
        item = company.objects.get(pk=pk) 

        serializer = companySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        item = company.objects.get(pk=pk)  
        item.delete()

        return Response(
            {"message": "Company deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
class DepartmentAPIView(APIView):
    # GET (list)
    def get(self, request):
        items = Department.objects.all()
        serializer = DepartmentSerializer(items, many=True) 
        return Response(serializer.data) 

    # POST (create)
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentupdateAPIView(APIView):
    def put(self, request, pk):
        item = Department.objects.get(pk=pk) 

        serializer = DepartmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        item = Department.objects.get(pk=pk)  
        item.delete()

        return Response(
            {"message": "Department deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
class employeeAPIView(APIView):
    # GET (list)
    def get(self, request):
        items = employee.objects.all()
        serializer = employeeSerializer(items, many=True) 
        return Response(serializer.data) 

    # POST (create)
    def post(self, request):
        serializer = employeeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class employeeupdateAPIView(APIView):
    def put(self, request, pk):
        item = employee.objects.get(pk=pk) 

        serializer = employeeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        item = employee.objects.get(pk=pk)  
        item.delete()

        return Response(
            {"message": "employee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class TaskAPIView(APIView):
    # GET (list)
    def get(self, request):
        items = Task.objects.all()
        serializer = TaskSerializer(items, many=True) 
        return Response(serializer.data) 

    # POST (create)
    def post(self, request):
        serializer = TaskSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskupdateAPIView(APIView):
    def put(self, request, pk):
        item = employee.objects.get(pk=pk) 

        serializer = TaskSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        item = Task.objects.get(pk=pk)  
        item.delete()

        return Response(
            {"message": "Task deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class TaskFilterAPIView(APIView):
    def get(self, request,task_status):
        query = Task.objects.all()

        if task_status != "null":
            query = query.filter(task_status=task_status)
        serializer = TaskSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


es = Elasticsearch("http://localhost:9200")

class EmployeeSearchAPIView(APIView):
    def get(self, request):
        name = request.query_params.get("name")
        designation = request.query_params.get("designation")
        company_id = request.query_params.get("company")
        department_id = request.query_params.get("department")

        must = []
        filter_query = []

        # Name search (partial, autocomplete)
        if name:
            must.append({
                "match": {
                    "name": name
                }
            })

        #  Designation filter (case-insensitive)
        # if designation:
        #     filter_query.append({
        #         "match": {
        #             "designation": designation
        #         }
        #     })

        if designation:
            must.append({
                "match": {
                    "designation": designation
                }
            })

        if company_id:
            filter_query.append({
                "term": {
                    "company.id": company_id
                }
            })

        #  Department filter (exact UUID)
        if department_id:
            filter_query.append({
                "term": {
                    "Department.id": department_id
                }
            })

        query = {
            "bool": {
                "must": must,
                "filter": filter_query
            }
        }

        result = es.search(
            index="employees",
            body={"query": query}
        )

        return Response([hit["_source"] for hit in result["hits"]["hits"]]) 
