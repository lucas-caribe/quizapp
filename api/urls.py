from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryView)
router.register(r'questions', views.QuestionView)
router.register(r'answers', views.AnswerView)

urlpatterns = router.urls
