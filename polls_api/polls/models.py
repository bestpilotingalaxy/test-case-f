from django.db import models as m


class Poll(m.Model):
    
    name = m.CharField('Название', max_length=200)
    start_date = m.DateTimeField('Дата старта')
    end_date = m.DateTimeField('Дата окончания')
    description = m.TextField('Описание', max_length=1000, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы' 
        

class Question(m.Model):
    """
    """
    
    QUESTION_TYPES = [
        ('text_response', 'Ответ текстом'),
        ('single_choice', 'Ответ с выбором одного варианта'),
        ('multiple_choice', 'Ответ с выбором нескольких вариантов')
    ]
    
    poll = m.ForeignKey(Poll, verbose_name='Опрос', on_delete=m.CASCADE)
    text = m.TextField('Текст вопроса', max_length=200)
    question_type = m.CharField(
        'Тип вопроса',
        max_length=15,
        choices=QUESTION_TYPES,
        default='single_choice'
    )

    def __str__(self):
        return f'{self.poll} -- {self.text}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    

class Answer(m.Model):
    """
    """
    
    question = m.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=m.CASCADE
    )
    text = m.CharField('Текст ответа', max_length=200)
    
    def __str__(self):
        return f'{self.question} -- {self.text}'
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'