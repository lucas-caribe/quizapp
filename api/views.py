from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from random import choices

from .serializers import AnswerSerializer, CategorySerializer, QuestionSerializer
from .models import Answer, Category, Question

@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
  return JsonResponse({ 'message': 'Hello World!' })

# get categories
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_categories(request):
  categories = Category.objects.all()
  serializer = CategorySerializer(categories, many=True)

  return JsonResponse({ 'categories': serializer.data }, safe=False, status=status.HTTP_200_OK)

# get questions
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_questions(request):
  questions = Question.objects.all()
  serializer = QuestionSerializer(questions, many=True)
  
  if len(serializer.data) > 5:
    random_questions = choices(serializer.data, k=5)
  else:
    random_questions = serializer.data

  return JsonResponse({ 'questions': random_questions }, safe=False, status=status.HTTP_200_OK)

# get answers
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_answers(request, question_id):
  answers = Answer.objects.filter(question_id=question_id)
  serializer = AnswerSerializer(answers, many=True)

  return JsonResponse({ 'answers': serializer.data }, safe=False, status=status.HTTP_200_OK)
