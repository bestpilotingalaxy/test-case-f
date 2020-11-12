from django.contrib import admin
from .models import Poll, Question, Answer, Variant


class VariantInline(admin.TabularInline):
    """"""
    model = Variant


class QuestionInline(admin.StackedInline):
    """
    Inline representation for questions.
    """
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        VariantInline,
    ]
    class Meta:
        model = Question


class PollAdmin(admin.ModelAdmin):
    """
    Adds action which create new questions in Poll admin panel.
    """
    inlines = [
        QuestionInline,
    ]
    # block start_date field for changing after object creation
    # readonly_fields = ('start_date', )
    
    class Meta:
        model = Poll


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Variant)