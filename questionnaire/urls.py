from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import QuestionView, QuestionnaireView, AnswerOptionsView, ResultQuestionnaireView


router = DefaultRouter()
router.register(r'blanks', QuestionnaireView, basename='Questionnaire')
router.register(r'questions', QuestionView, basename='Question')
router.register(r'answer_options', AnswerOptionsView, basename='AnswerOptions')
router.register(r'result_questionnaire', ResultQuestionnaireView, basename='ResultQuestionnaire')


urlpatterns = router.urls


