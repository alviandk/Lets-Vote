from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("result/<uuid:question_id>", views.result, name="result"),
    path("vote/<uuid:question_id>", views.vote, name="vote"),
]