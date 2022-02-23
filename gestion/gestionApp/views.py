from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer
from .models import Client

# Create your views here.


@api_view(['GET'])
def allClients(request):
    clients = Client.objects.all()
    serialization = ClientSerializer(clients,many=True)
    return Response(serialization.data)

@api_view(['GET'])
def getClient():
    client = Client.objects.get(id=id)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

# @api_view(['POST'])