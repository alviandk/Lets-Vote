from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Question, Choice

class QuestionViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.question = Question.objects.create(text="Sample Question")
        self.choice1 = Choice.objects.create(text="Choice 1", question=self.question)
        self.choice2 = Choice.objects.create(text="Choice 2", question=self.question)

    def test_index_view(self):
        url = reverse('index')  # Assuming 'index' is the name of your index view in urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # As we've added 1 question in setUp

    def test_result_view(self):
        url = reverse('result', args=[self.question.id])  # Assuming 'result' is the name of your result view in urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vote_view(self):
        # Test with valid data
        url = reverse('vote', args=[self.question.id])  # Assuming 'vote' is the name of your vote view in urls.py
        response = self.client.post(url, {"choice_id": self.choice1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "vote submitted")

    def test_vote_view_without_choice_id(self):
        url = reverse('vote', args=[self.question.id])
        # Test without choice_id
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "choice_id required!")

    def test_vote_view_with_nonexistent_choice_id(self):
        url = reverse('vote', args=[self.question.id])
        # Test with invalid data (nonexistent choice_id for example)
        response = self.client.post(url, {"choice_id": 999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "request data invalid!")
