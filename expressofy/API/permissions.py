from django.conf import settings
from django.urls import resolve
from rest_framework import permissions

from rest_framework.permissions import BasePermission

class Check_API_KEY(BasePermission):
    def has_permission(self, request, view):
        func, args, kwargs = resolve(request.get_full_path())
        api_key=kwargs.get('api_key',"wrong_api_key")
        return api_key == settings.API_KEY
        