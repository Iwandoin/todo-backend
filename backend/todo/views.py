from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.http import HttpResponse
# Create your views here.
import boto3
import time
import os
import socket
from botocore.exceptions import NoCredentialsError



class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# Create your views here.
AWS_ACCESS_KEY = os.environ.get("AWS_S3_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_S3_SECRET_KEY")

def return_objects(request):
    yes = 'Host:' + socket.gethostname() + ' , file uploaded test'
    no = 'Host:' + socket.gethostname() + ' , file not uploaded test'
    empty = 'Host:' + socket.gethostname() + ' , there is no todos test'
    queryset = Todo.objects.all()
    d = len(queryset)
    if d == 0:
        return HttpResponse(empty)
    # open and read the file:
    f = open("file.txt", "w+")
    #print(f.read())
    for x in queryset:
        b1 = '|{:' '^5}|'.format(str(x.id))
        b2 = '{:' '^50}|'.format(str(x.title))
        b3 = '{:' '^100}|'.format(str(x.description))
        b4 = '{:' '^5}|'.format(str(x.completed))
        c = b1 + b2 + b3 + b4 + '\n'
        f.write(c)
    f.close()
    timestr = time.strftime("%Y%m%d-%H_%M_%S")
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.upload_file('file.txt', 'myvyadro', timestr)
        print("Upload Successful")
        return HttpResponse(yes)
    except :
        return HttpResponse(no)
    #
