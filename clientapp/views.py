from django.shortcuts import render
from superadmin.models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics

# Create your views here.

class RegisterUserView(views.APIView):
 
    def post(self, request, *args, **kwargs):
        serializer = TenantRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User, tenant, and domain created successfully", "user": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








