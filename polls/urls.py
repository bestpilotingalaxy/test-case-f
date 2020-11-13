from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    
    # Polls CRUD
    path('poll/<int:pk>/', views.PollViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    )),    
    path('polls/', views.PollViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    # Question CRUD
    path('question/', views.QuestionViewSet.as_view(
        {
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    )),
    # Answers urls
    path('answer/', views.CreateAnswerView.as_view()),
    path('answers/<int:pk>/', views.AnswerListView.as_view()),
])
