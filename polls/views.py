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
    AnswerCreateSerializer
)


class PollViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Full CRUD and List sctions for Poll model.
    """
    queryset = Poll.objects.all()

    def list(self, request):
        """
        List action with queryset filters by date.
        Query only active polls.
        """
        if self.request.user.is_staff:
            queryset = Poll.objects.all()
        else:    
            queryset = Poll.objects.filter(
                start_date__lte=datetime.datetime.today(),
                end_date__gte=datetime.datetime.today()
            )
        serializer = UpdatePollSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        """
        Select permission class based on request action.
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [permissions.IsAdminUser] 
        else:
            permission_classes = [permissions.AllowAny]
        
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Select serializer class based on request action.
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
    Create, Update, Destroy actions for Question model.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [permissions.IsAdminUser,]


class AnswerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    """
    serializer_class = AnswerCreateSerializer
    
    def get_serializer_context(self):
        """
        Add anonimous user session key to serializer context.
        """
        context = super(AnswerViewSet, self).get_serializer_context()
        context.update({'session_key': self.request.session.session_key, 'poll': Poll.objects.get(pk=self.kwargs['pk'])})
        return context
    
    def get_queryset(self):
        """
        Filter answers by user session key and poll_id from request kwargs.
        """
        session_key = self.request.session.session_key
        queryset = Answer.objects.filter(
            session_key=session_key,
            poll=self.kwargs['pk']
        )
        return queryset