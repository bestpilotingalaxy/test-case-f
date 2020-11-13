from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    path('poll/<int:pk>/', views.PollViewSet.as_view(
        {'get': 'retrieve','post': 'create', 'put': 'update', 'delete': 'destroy'}
    )),    
    path('polls/', views.PollViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('question/', views.QuestionViewSet.as_view(
        {'post': 'create', 'put': 'update', 'delete': 'destroy'}
    )),
    path('answer/', views.AnswerViewSet.as_view()),

])
