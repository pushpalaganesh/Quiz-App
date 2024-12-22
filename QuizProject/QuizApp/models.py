from django.db import models
import uuid
import random


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Type(BaseModel):
    objects = None
    gfg_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.gfg_name


class Question(BaseModel):
    objects = None
    gfg = models.ForeignKey(Type, related_name='gfg', on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for i in answer_objs:
            data.append({
                'answer': i.answer,
                'is_correct': i.is_correct
            })
        return data


class Answer(BaseModel):
    objects = None
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
