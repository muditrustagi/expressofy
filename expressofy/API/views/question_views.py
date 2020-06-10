from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from API.permissions import Check_API_KEY
from ..serializer import QuestionSerializer
from . import helper_functions
from ..models import * 
import traceback


@api_view(['GET','POST'])
@permission_classes((Check_API_KEY, ))
def question_controller(request,api_key,control_word):
	return helper_functions.data_controller(request,control_word,Question,QuestionSerializer,'question_id')