from django.core.exceptions import ValidationError
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models


@api_view(['GET'])
def index(request):
    questions_list = models.Question.objects.to_dict_list()
    return Response(questions_list)


@api_view(['GET'])
def result(request, question_id):
    question = models.Question.objects.get(id=question_id)
    return Response(question.get_choice_percentages())


@api_view(['POST'])
def vote(request, question_id):
    choice_id = request.data.get("choice_id")
    if not choice_id:
        return Response({"message": "choice_id required!"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        models.VoteChoice.objects.create(
            question_id=question_id,
            choice_id=choice_id
        )
        return Response({"message": "vote submitted"})
    except ValidationError:
        return Response({"message": "request data invalid!"}, status=status.HTTP_400_BAD_REQUEST)