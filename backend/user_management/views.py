from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import UserSerializer
from rest_framework import generics, status


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    data = request.data
    user_type = data['type']
    if user_type == 'member':
        try:
            user = User.objects.get(email=data['email'])
            if user.is_active:
                return Response({'message': 'User already exists'})
        except User.DoesNotExist:
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response({'message': 'Saved Successfully'})
            return Response({'message': 'failed to save'})
    elif user_type == 'admin':
        try:
            user = User.objects.get(email=data['email'])
            if user.is_active:
                return Response({'message': 'User already exists'})
        except User.DoesNotExist:
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response({'message': 'Saved successfully'})
            return Response({'message': 'failed to save'})
