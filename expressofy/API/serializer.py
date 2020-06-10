from rest_framework import serializers
from .models import User,Bookmark,Interest,Question,Intro_Video

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields='__all__'

class BookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model=Bookmark
		fields='__all__'

class InterestSerializer(serializers.ModelSerializer):
	class Meta:
		model=Interest
		fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Question
		fields='__all__'

class IntroVideoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Intro_Video
		fields='__all__'