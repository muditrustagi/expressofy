from django.db import models

STATE_CHOICES = ((0,"INACTIVE"),(1,"ACTIVE"),(2,"BLOCKED"))
IS_PREMIUM_CHOICES = ((0,"FREEMIUM"),(1,"PREMIUM"))

class User(models.Model):
    user_id                     =   models.AutoField(primary_key=True, auto_created = True)
    user_joined_on              =   models.DateTimeField(auto_now_add=True,null=True)
    user_profile_image          =   models.ImageField(blank=True)
    user_name                   =   models.CharField(max_length=40,blank=False,null=False)
    user_bio                    =   models.TextField(max_length=100,blank=True)
    user_gender                 =   models.CharField(max_length=20,blank=False,null=False)
    user_phone_number           =   models.CharField(max_length=20,blank=False,null=False)
    user_profession             =   models.CharField(max_length=20,blank=False,null=False)
    user_email                  =   models.EmailField(blank=False,null=False)
    user_dob                    =   models.DateTimeField(blank=False,null=False)
    user_fcoin                  =   models.CharField(default=0,max_length = 20)
    user_state                  =   models.IntegerField(default=1)
    user_interests              =   models.CharField(max_length=100,blank=True)
    user_is_premium             =   models.IntegerField(default=0)
    

class Bookmark(models.Model):
    bookmark_id                 =   models.AutoField(primary_key=True, auto_created = True)
    user                        =   models.ForeignKey('User',on_delete=models.CASCADE)
    bookmark                    =   models.TextField()
    

class Interest(models.Model):
    interest_id                 =   models.AutoField(primary_key=True, auto_created = True)
    interest_created_on         =   models.DateTimeField(auto_now_add=True)   
    interest_name               =   models.CharField(max_length=40)
    interest_image              =   models.ImageField(blank=True)
    interest_desc               =   models.TextField(blank=True)


class Question(models.Model):
    question_id                 =   models.AutoField(primary_key=True, auto_created = True)
    question_question           =   models.TextField()
    question_options            =   models.TextField()
    question_correct_answer     =   models.TextField()
    question_created_on         =   models.DateTimeField(auto_now_add=True)
    

class Intro_Video(models.Model):
    intro_video_id              =   models.AutoField(primary_key=True, auto_created = True)
    intro_video                 =   models.FileField(upload_to='uploads/')
    intro_created_on            =   models.DateTimeField(auto_now_add=True)
    intro_desc                  =   models.TextField(blank=True)

