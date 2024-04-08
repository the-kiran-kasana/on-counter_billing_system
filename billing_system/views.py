from django.shortcuts import render
from rest_framework import generics
from .models import Employee, Product, Customer, Bill
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BillListCreate(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
