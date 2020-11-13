from django.contrib import admin
from .models import Poll, Question, Answer, Variant


class VariantInline(admin.TabularInline):
    """
    Inline representation for variant.
    """
    model = Variant


class QuestionInline(admin.TabularInline):
    """
    Inline representation for questions.
    """
    model = Question


class PollAdmin(admin.ModelAdmin):
    """
    Adds action which create new questions in Poll admin panel.
    """
    inlines = [
        QuestionInline, VariantInline
    ]
    
    class Meta:
        model = Poll


admin.site.register(Poll, PollAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Variant)