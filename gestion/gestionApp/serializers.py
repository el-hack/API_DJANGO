from rest_framework import serializers
from .models import Client, Service, Typeabo

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fiels = '__all__'
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fiels = '__all__'
        
        
class TypaboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeabo
        fiels = '__all__'
    
    