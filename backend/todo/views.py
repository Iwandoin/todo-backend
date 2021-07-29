from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.http import HttpResponse
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


# Create your views here.


def return_objects(request):
    #text = """<h1>Hello World!</h1>"""
    #return HttpResponse(text)
    #serializer_class = TodoSerializer
    queryset = Todo.objects[5].title
    return HttpResponse(queryset)