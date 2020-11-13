from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, ListSerializer

from .models import Poll, Question, Answer, Variant


class AnswerDetailSerializer(ModelSerializer):
    """
    Serialize answer, prevent duplicate answering and get user session key.
    """
    class Meta:
        model = Answer
        exclude = ('session_key',)
    
    def save(self, **kwargs):
        super().save(session_key=self.context['session_key'])
    
    def validate(self, attrs):
        """
        Validate if user already answer the question.
        """
        answer = Answer.objects.filter(
            question_id=attrs['question'],
            session_key=self.context['session_key']
        )
        if answer:
            raise ValidationError('You already answeren this question.')
        return attrs
    

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
    Serialize questions and gets serialized variants of answers. 
    """
    variants = VariantDetailSerializer(many=True)
    
    class Meta:
        model = Question
        fields = '__all__'
    
    
class PollDetailSerializer(ModelSerializer):
    """
    Poll detail serializer.
    Starts recursive tree serializing, gets all poll questions and variants.
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