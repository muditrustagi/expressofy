from django.contrib import admin
from .models import *


admin.site.register(User, list_display = ['user_id', 'user_name'])
admin.site.register(Bookmark, list_display = ['bookmark_id'])
admin.site.register(Interest, list_display = ['interest_id'])
admin.site.register(Question, list_display = ['question_id'])
admin.site.register(Intro_Video, list_display = ['intro_video_id'])


