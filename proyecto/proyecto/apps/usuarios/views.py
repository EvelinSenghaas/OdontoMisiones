from django.shortcuts import render
from django.contrib.auth.models import Permission
from rest_framework_jwt.utils import jwt_payload_handler

# Create your views here.
def jwt_custom_payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['permissions'] = [(x.codename) for x in Permission.objects.filter(user=user)]
    return payload
