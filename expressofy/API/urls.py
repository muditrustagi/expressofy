from django.urls import path
from .views import *
  
urlpatterns = [
    path('<str:api_key>/user/<str:control_word>',           user_views.user_controller,             name='user_index'),
    path('<str:api_key>/user/bookmark/<str:control_word>',  user_views.user_bookmark_controller,     name='bookmark_index'),
    path('<str:api_key>/interest/<str:control_word>',       interest_views.interest_controller,     name='interest_index'),
    path('<str:api_key>/question/<str:control_word>',       question_views.question_controller,     name='question_index'),
    path('<str:api_key>/intro-video/<str:control_word>',    video_views.intro_video_controller,     name='intro_video_index'),

]