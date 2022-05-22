from django.contrib import admin
from django.urls import path

from softfactory.views import *

urlpatterns = [
    path('mealsitems/', MealItemsView.as_view()),
    path('categoryitems/', CategoryItemsView.as_view()),
    path('meals/', MealsView.as_view())
]