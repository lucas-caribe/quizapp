from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from random import sample

from .serializers import AnswerSerializer, CategorySerializer, QuestionSerializer
from .models import Answer, Category, Question

MAX_QUESTIONS = 5

class CategoryView(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class AnswerView(viewsets.ModelViewSet):
  serializer_class = AnswerSerializer
  queryset = Answer.objects.all()

class QuestionView(viewsets.ModelViewSet):
  serializer_class = QuestionSerializer
  queryset = Question.objects.all()

  @action(detail=False)
  def random(self, request):
    queryset = self.get_queryset()
    questions = queryset.all()
    serializer = QuestionSerializer(questions, many=True)

    if len(serializer.data) > MAX_QUESTIONS:
      random_questions = sample(serializer.data, MAX_QUESTIONS)
    else:
      random_questions = serializer.data

    return Response(random_questions)
