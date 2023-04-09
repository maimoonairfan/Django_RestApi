from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo_app.serializers import ProductSerializer, ProductSerializer
from todo_app.models import Product

# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer