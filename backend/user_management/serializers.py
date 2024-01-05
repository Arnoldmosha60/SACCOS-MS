from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'type',
            'password',
            'contact',
            'date_joined',
            'username',
        ]
        extra_kwargs = {"password": {"write_only": True}}

        def __init__(self):
            self.validated_data = None

        def create(self, validated_data):
            if self.validated_data['type'] == 'member':
                print('Iam member')
                email = self.validated_data['email']
                full_name = self.validated_data['full_name']
                username = self.validated_data['username']
                password = self.validated_data['password']
                contact = self.validated_data['contact']
                type = self.validated_data['type']
                date_joined = self.validated_data['date_joined']
                user = User.objects.create_user(email=email, full_name=full_name, username=username, password=password,
                                                contact=contact, type=type, date_joined=date_joined)
                return user
            elif self.validated_data['type'] == 'admin':
                print('Iam admin')
                email = self.validated_data['email']
                full_name = self.validated_data['full_name']
                username = self.validated_data['username']
                password = self.validated_data['password']
                contact = self.validated_data['contact']
                type = self.validated_data['type']
                date_joined = self.validated_data['date_joined']
                user = User.objects.create_user(email=email, full_name=full_name, username=username, password=password,
                                                contact=contact, type=type, date_joined=date_joined)
                return user
