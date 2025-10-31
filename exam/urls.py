from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('auto-submit-exam/', views.auto_submit_exam, name='auto_submit_exam'),
    path('exam-submitted/', views.exam_submitted, name='exam_submitted'),
]


