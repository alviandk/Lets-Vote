from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models


def index(request):
    return HttpResponse("Hello, world. You're at the votes index.")


@api_view(['GET'])
def result(request, question_id):
    
    if request.method == 'GET':
        question = models.Question.objects.get(id=question_id)
        return Response(question.get_choice_percentages())
