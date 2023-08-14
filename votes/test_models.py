from django.test import TestCase

from .models import Question, Choice, VoteChoice


class PollModelsTestCase(TestCase):

    def setUp(self):
        self.question = Question.objects.create(text="What's your favorite color?")
        self.choice_blue = Choice.objects.create(question=self.question, text="Blue")
        self.choice_red = Choice.objects.create(question=self.question, text="Red")

    def test_question_creation(self):
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(str(self.question), f'{self.question.id}: What\'s your favorite color?')

    def test_choice_creation(self):
        self.assertEqual(Choice.objects.count(), 2)
        self.assertEqual(str(self.choice_blue), f'{self.choice_blue.id}: Blue')

    def test_choice_percentages(self):
        VoteChoice.objects.create(question=self.question, choice=self.choice_blue)
        VoteChoice.objects.create(question=self.question, choice=self.choice_red)
        VoteChoice.objects.create(question=self.question, choice=self.choice_blue)
        
        self.assertEqual(VoteChoice.objects.count(), 3)

        # Check percentages
        percentages = self.question.get_choice_percentages()
        for p in percentages:
            if p['text'] == "Blue":
                self.assertEqual(p['votes_for_choice'], 2)
                self.assertEqual(p['percentage'], 66.66666666666667)  # 2 out of 3 votes is 66.67%
            elif p['text'] == "Red":
                self.assertEqual(p['votes_for_choice'], 1)
                self.assertEqual(p['percentage'], 33.333333333333336)  # 1 out of 3 votes is 33.33%

    def test_to_dict_list(self):
        result = Question.objects.to_dict_list()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['question']['text'], "What's your favorite color?")
        self.assertEqual(len(result[0]['question']['choices']), 2)
