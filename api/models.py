from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
  class Meta:
    verbose_name_plural = 'categories'
  name = models.CharField(max_length=150)

class Question(models.Model):
  content = models.CharField(max_length=500)
  score = models.PositiveSmallIntegerField()
  level = models.PositiveSmallIntegerField()
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Answer(models.Model):
  content = models.CharField(max_length=500)
  correct = models.BooleanField()
  question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
