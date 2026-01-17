from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import Stu_Serializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io   # for deserializer
from rest_framework.parsers import JSONParser
import json

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

        serializer = Stu_Serializer(data=py_data)   
        print(serializer)
        print(type(serializer))

        if serializer.is_valid():
            # print(serializer.validated_data)
            msg={'msg':'data saved'}
            jsmg_data=JSONRenderer().render(msg)
            serializer.save()
            return HttpResponse(jsmg_data , content_type='application/json')
        
        else:
            err_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(err_data, content_type='application/json')


    #---------------------------------GET DATA-----------------------------------------
    data=Student.objects.all()
    serializer=Stu_Serializer(data, many=True) # convert query set data into python by serializer
    print(serializer)
    print(serializer.data)
    json=JSONRenderer().render(serializer.data)  # convert python data into json data
    print(json)
    
    return HttpResponse(json, content_type='application/json')


@csrf_exempt
def stu_detail(req,pk):
    user = Student.objects.filter(id=pk)
    if user:
         #-------------------------------------PUT DATA-----------------------------------------

        if req.method=='PUT':
            j_data=req.body
            print(j_data)
            print(type(j_data))
            
            stream=io.BytesIO(j_data)  # jo data a rha h use hum byte io main convert kr rhe hai
            print(stream)
            print(type(stream))
        
            py_n_data=JSONParser().parse(stream)  # convert python data into json data
            print(py_n_data)
            py_o_data = Student.objects.get(id=pk)

            serializer = Stu_Serializer(py_o_data, data=py_n_data)
            # serializer = Stu_Serializer(py_o_data, data=py_n_data, partial=True)  # PUT act like PATCH if we use partial='True' so we dont need to define PATCH
            if serializer.is_valid():
                # print(serializer.validated_data)
                msg={'msg':'data updated succeessfully'}
                jsmg_data=JSONRenderer().render(msg)
                serializer.save()
                return HttpResponse(jsmg_data , content_type='application/json')
            
            else:
                err_data=JSONRenderer().render(serializer.errors)
                return HttpResponse(err_data, content_type='application/json')

       #-------------------------------------PATCH DATA-----------------------------------------
   
        elif req.method=='PATCH':
            j_data=req.body
            print(j_data)
            print(type(j_data))
            
            stream=io.BytesIO(j_data)  # jo data a rha h use hum byte io main convert kr rhe hai
            print(stream)
            print(type(stream))
        
            py_n_data=JSONParser().parse(stream)  # convert python data into json data
            print(py_n_data)
            py_o_data = Student.objects.get(id=pk)

            serializer = Stu_Serializer(py_o_data, data=py_n_data, partial=True)
            if serializer.is_valid():
                # print(serializer.validated_data)
                msg={'msg':'data saved'}
                jsmg_data=JSONRenderer().render(msg)
                serializer.save()
                return HttpResponse(jsmg_data , content_type='application/json')
            
            else:
                err_data=JSONRenderer().render(serializer.errors)
                return HttpResponse(err_data, content_type='application/json')
       
       #-------------------------------------DELETE DATA-----------------------------------------

        elif req.method=="DELETE":
            py_o_data = Student.objects.get(id=pk)
            py_o_data.delete()
            msg={'msg':'data deleted'}
            jsmg_data=JSONRenderer().render(msg)
            return HttpResponse(jsmg_data , content_type='application/json')
    else:
        msg={'msg':'user not found'}
        jsmg_data=JSONRenderer().render(msg)
        return HttpResponse(jsmg_data , content_type='application/json')
    #-------------------------------------GET DATA------------------------------------------
    data=Student.objects.get(id=pk)
    serializer=Stu_Serializer(data) # convert query set data into python by serializer
    print(serializer)
    print(serializer.data)
    json=JSONRenderer().render(serializer.data)  # convert python data into json data
    print(json)
    
    return HttpResponse(json, content_type='application/json')
