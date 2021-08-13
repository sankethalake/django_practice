from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("--------list--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("--------retrieve--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("--------create--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("--------update--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print("--------partial_update--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partially updated'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        print("--------delete--------")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Deleted'})
