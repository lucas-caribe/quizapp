from rest_framework import serializers
from .models import Category, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ['id', 'content', 'score', 'level', 'category_id']

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = ['id', 'content', 'correct', 'question_id']
