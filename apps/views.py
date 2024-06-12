from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializers
from.models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fileds=['city']

    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    
        
