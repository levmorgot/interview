from django.db import models
from django.utils import timezone


class Questionnaire(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()


class Question(models.Model):
    TEXT = 'T'
    ONE = 'O'
    SOME = 'S'
    question = models.TextField()
    questionnaires = models.ManyToManyField(Questionnaire)
    TYPE_CHOICES = [
        (TEXT, 'text'),
        (ONE, 'one'),
        (SOME, 'some'),
    ]
    year_in_school = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=TEXT,
    )


class AnswerOptions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=25)


class ResultQuestionnaire(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=25)
