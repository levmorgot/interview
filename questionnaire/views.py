from rest_framework import viewsets
from .serializers import *


class QuestionnaireView(viewsets.ModelViewSet):

    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()


class QuestionView(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerOptionsView(viewsets.ModelViewSet):

    serializer_class = AnswerOptionsSerializer
    queryset = AnswerOptions.objects.all()


class ResultQuestionnaireView(viewsets.ModelViewSet):

    serializer_class = ResultQuestionnaireSerializer
    queryset = ResultQuestionnaire.objects.all()
