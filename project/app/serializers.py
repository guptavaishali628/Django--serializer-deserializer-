from rest_framework import serializers  # import serializers after installing 'pip install djangorestframework'

class Stu_Serializer(serializers.Serializer):   # syntax same as model, form :
    name=serializers.CharField()
    email=serializers.EmailField()
    city=serializers.CharField()