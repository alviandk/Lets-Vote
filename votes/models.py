import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Count, FloatField, ExpressionWrapper, F, OuterRef, Subquery


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class Question(BaseModel):
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.text}'

    def get_choice_percentages(self):
        # Subquery for total votes of the given question.
        total_votes_for_question = VoteChoice.objects.filter(question=self).values('question').annotate(total=Count('id')).values('total')

        # Annotate each choice with its vote count and the total votes for its question, and retrieve only choice text and percentage.
        choices = Choice.objects.filter(question=self).annotate(
            votes_for_choice=Count('votechoice'),
            total_votes_for_question=Subquery(total_votes_for_question, output_field=FloatField())
        ).annotate(
            percentage=ExpressionWrapper(
                F('votes_for_choice') * 100.0 / F('total_votes_for_question'),
                output_field=FloatField()
            )
        ).values_list('text', 'percentage')

        return list(choices)



class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.text}'


class VoteChoice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.text} {self.choice.text}'
