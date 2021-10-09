from rest_framework import routers
from .api import FoodViewSet, CategoryViewSet, FoodItemViewSet, DayViewSet, DailyCalorieIntakeViewSet
from django.urls import path, re_path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
]

router = routers.DefaultRouter()
router.register('api/foods', FoodViewSet, 'foods')
router.register('api/days', DayViewSet, 'days')
router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/food-items', FoodItemViewSet, 'food-items')
router.register('api/daily-calorie-intake', DailyCalorieIntakeViewSet, 'daily-calorie-intake')

urlpatterns += router.urls