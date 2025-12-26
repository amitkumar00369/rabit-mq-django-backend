from django.shortcuts import render
from django.http import HttpResponse

from rabbit.producer import public_message

from rest_framework.response import Response
from rest_framework.views import APIView
class HelloWorld(APIView):
    def get(self,request):
        message = request.query_params.get('message')
        userType = request.query_params.get('userType')
        pub_message = public_message({'message':message,'userType':userType})

        return Response({'data':{'message':message,'userType':userType}})
