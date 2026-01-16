from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import Stu_Serializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io   # for deserializer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def stu_list(req):
    #---------------------------------POST DATA----------------------------------------
    if req.method=='POST':
        j_data=req.body
        print(j_data)
        print(type(j_data))
        
        stream=io.BytesIO(j_data)  # jo data a rha h use hum byte io main convert kr rhe hai
        print(stream)
        print(type(stream))
       
        py_data=JSONParser().parse(stream)  # convert python data into json data
        print(py_data)

        dserializer = Stu_Serializer(data=py_data)   
        print(dserializer)
        print(type(dserializer))

        if dserializer.is_valid():
            dserializer.save()
            return HttpResponse({'msg':'data.save'})


    #---------------------------------GET DATA-----------------------------------------
    # data=Student.objects.all()
    # serializer=Stu_Serializer(data, many=True) # convert query set data into python by serializer
    # print(serializer)
    # print(serializer.data)
    # json=JSONRenderer().render(serializer.data)  # convert python data into json data
    # print(json)
    
    # return HttpResponse(json, content_type='application/json')

def stu_detail(req,pk):
    #-------------------------------------GET DATA------------------------------------------
    data=Student.objects.get(id=pk)
    serializer=Stu_Serializer(data) # convert query set data into python by serializer
    print(serializer)
    print(serializer.data)
    json=JSONRenderer().render(serializer.data)  # convert python data into json data
    print(json)
    
    return HttpResponse(json, content_type='application/json')
