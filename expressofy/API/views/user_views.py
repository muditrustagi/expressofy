from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from API.permissions import Check_API_KEY
from ..serializer import UserSerializer
from ..serializer import BookmarkSerializer
from . import helper_functions
from ..models import * 
import traceback


@api_view(['GET','POST'])
@permission_classes((Check_API_KEY, ))
def user_controller(request,api_key,control_word):
	return helper_functions.data_controller(request,control_word,User,UserSerializer,'user_id')


@api_view(['GET','POST'])
@permission_classes((Check_API_KEY, ))
def user_bookmark_controller(request,api_key,control_word):
	return helper_functions.data_controller(request,control_word,Bookmark,BookmarkSerializer,'bookmark_id')