from django.shortcuts import render
from myapp.serializers import CustomerSerializer
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def CustomerList(request):
    if request.method == "GET":
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many = True)

        return Response(serializer.data)

    if request.method == 'POST':
        
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
