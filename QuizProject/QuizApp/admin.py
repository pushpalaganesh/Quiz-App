from django.contrib import admin
from .models import *


# Register your models here.
class AnswerAdmin(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Type)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
