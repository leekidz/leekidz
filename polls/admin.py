from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,          {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
