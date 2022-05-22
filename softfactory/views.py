from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class MealItemsView(APIView):

    def get(self, request):
        mealitems = MealsItems.objects.all()
        mealitems_ser = MealItemsSerializer(mealitems, many=True).data
        return Response({'data': mealitems_ser}, status=status.HTTP_200_OK)

    def post(self, request):
        mealitems_ser = MealItemsSerializer(data=self.request.data)
        mealitems_ser.is_valid()
        mealitems_ser.save()
        return Response({'status': True}, status=status.HTTP_201_CREATED)


class CategoryItemsView(APIView):

    def get(self, request):
        categoryitems = CategoryItems.objects.all()
        categoryitems_ser = CategoryItemsSerializer(categoryitems, many=True).data
        return Response({'data': categoryitems_ser}, status=status.HTTP_200_OK)

    def post(self, request):
        categoryitems_set = CategoryItemsSerializer(data=self.request.data)
        categoryitems_set.is_valid()
        categoryitems_set.save()
        return Response({'status': True}, status=status.HTTP_201_CREATED)


class MealsView(APIView):

    def get(self, request):
        meals = Meals.objects.all()
        meals_ser = MealsSerializer(meals, many=True).data
        return Response({'data': meals_ser}, status=status.HTTP_200_OK)

    def post(self, request):
        meals_ser = MealsSerializer(data=self.request.data)
        meals_ser.is_valid()
        meals_ser.save()
        return Response({'status': True}, status=status.HTTP_201_CREATED)
