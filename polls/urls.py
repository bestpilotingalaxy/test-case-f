from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    
    # Answers urls
    path('polls/<int:pk>/answers/', views.AnswerViewSet.as_view(
        {
            'post': 'create',
            'get': 'list'
        }
    )),
    # Polls CRUD
    path('polls/<int:pk>/', views.PollViewSet.as_view(
        {
            'get': 'retrieve',
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
    path('questions/<int:pk>/', views.QuestionViewSet.as_view(
        {
            'put': 'update',
            'delete': 'destroy'
        }
    )),
    path('questions/', views.QuestionViewSet.as_view(
        {
            'post': 'create'
        }
    )),
])
