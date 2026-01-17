from rest_framework import serializers  # import serializers after installing 'pip install djangorestframework'
from .models import Student
class Stu_Serializer(serializers.Serializer):   # syntax same as model, form :
    name=serializers.CharField()
    email=serializers.EmailField()
    city=serializers.CharField()
    
    #copy paste DRF code
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
