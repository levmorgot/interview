from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'questionnaires', 'year_in_school')


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'title', 'description', 'start_date', 'end_date')


class AnswerOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOptions
        fields = ('id', 'question', 'value')


class ResultQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultQuestionnaire
        fields = ('id', 'questionnaire', 'question', 'value')


