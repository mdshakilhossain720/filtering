from django.shortcuts import render
from rest_framework.serializers import StudetnSerilazer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class Studentlist(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudetnSerilazer
    pagination_class=
