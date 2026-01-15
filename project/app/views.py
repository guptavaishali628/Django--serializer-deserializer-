from django.shortcuts import render
from .models import Student
from .serializers import Stu_Serializer

# Create your views here.

def stu_list(req):
    data=Student.objects.all()
    serializer=Stu_Serializer(data, many=True)
    print(serializer)
    print(serializer.data)
