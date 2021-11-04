from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getcategories', views.get_categories),
  path('getquestions', views.get_questions),
  path('getanswers/<int:question_id>', views.get_answers),
  path('addquestion', views.add_question),
]
