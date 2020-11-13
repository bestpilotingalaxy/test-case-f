from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ListSerializer

from .models import Poll, Question, Answer, Variant


# class AnswerDetailSerializer(ModelSerializer):
#     class Meta:
#         model = Answer
#         exclude = ('user_id',)
    
#     def save(self, **kwargs):
#         super().save(session=self.context['session'])


class VariantDetailSerializer(ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class QuestionDetailSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionTreeSerializer(ModelSerializer):
    """
    """
    variants = VariantDetailSerializer(many=True)
    
    class Meta:
        model = Question
        fields = '__all__'
    
    
class PollDetailSerializer(ModelSerializer):
    """
    """
    questions = QuestionTreeSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            'name', 'start_date', 'end_date',
            'description', 'questions'
        )


class UpdatePollSerializer(ModelSerializer):
    
    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ('start_date',)