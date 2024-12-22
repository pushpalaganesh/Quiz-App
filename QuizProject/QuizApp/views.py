from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
import random


# Create your views here.
def home(request):
    t = Type.objects.all()
    context = {'data': t}
    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")
    return render(request, 'home.html', context)


def quiz(request):
    context = {'gfg': request.GET.get('gfg')}
    return render(request, 'quiz.html', context)


def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('gfg'):
            question_objs = question_objs.filter(gfg__gfg_name__icontains=request.GET.get('gfg'))
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        for i in question_objs:
            data.append({
                "uid": i.uid,
                "gfg": i.gfg.gfg_name,
                "question": i.question,
                "marks": i.marks,
                "answer": i.get_answers(),
            })
        payload = {'status': True, 'data': data}
        print("Payload:", payload)  # Debugging statement
        return JsonResponse(payload)
    except Exception as e:
        print("Error:", e)  # Log the error for debugging
        return HttpResponse("Something went wrong")
