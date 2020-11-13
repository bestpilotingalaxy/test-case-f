import datetime

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import Answer, Poll, Question
from .serializers import (
    PollDetailSerializer,
    UpdatePollSerializer,
    QuestionDetailSerializer,
    AnswerDetailSerializer
)


class PollViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    """
    queryset = Poll.objects.all()

    def list(self, request):
        queryset = Poll.objects.filter(
            start_date__lte=datetime.datetime.today(),
            end_date__gte=datetime.datetime.today()
        )
        serializer = UpdatePollSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        """
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [permissions.IsAdminUser] 
        else:
            permission_classes = [permissions.AllowAny]
        
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        """
        if self.action=='update':
            serializer_class = UpdatePollSerializer
        else:
            serializer_class = PollDetailSerializer
        
        return serializer_class

  
class QuestionViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    """
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    
    def get_permissions(self):
        """
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [permissions.IsAdminUser] 
        else:
            permission_classes = [permissions.AllowAny]
        
        return [permission() for permission in permission_classes]


# class AnswerViewSet(CreateAPIView):
#     """
#     """
#     queryset = Answer.objects.all()
#     serializer_class = AnswerDetailSerializer
    
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({"session": self.request.session.session_key})
#         return context