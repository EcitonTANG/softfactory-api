from django.db import models


class MealsItems(models.Model):
    strMeal = models.CharField(max_length=128, blank=True, null=True)
    strMealThumb = models.TextField(blank=True, null=True)
    idMeal = models.IntegerField(primary_key=True)


class CategoryItems(models.Model):
    idCategory = models.IntegerField(primary_key=True)
    strCategory = models.CharField(max_length=128, blank=True, null=True)
    strCategoryThumb = models.TextField(blank=True, null=True)
    strCategoryDescription = models.TextField(blank=True, null=True)


class Meals(models.Model):
    idMeal = models.IntegerField(primary_key=True)
    strMeal = models.CharField(max_length=128, blank=True, null=True)
    strCategory = models.CharField(max_length=128, blank=True, null=True)
    strInstruction = models.TextField(blank=True, null=True)
    strMealThumb = models.TextField(blank=True, null=True)
    strTags = models.CharField(max_length=128, blank=True, null=True)
    strIngredient1 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient2 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient3 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient4 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient5 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient6 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient7 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient8 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient9 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient10 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient11 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient12 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient13 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient14 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient15 = models.CharField(max_length=128, blank=True, null=True)
    strIngredient16 = models.CharField(max_length=128)
    strIngredient17 = models.CharField(max_length=128)
    strIngredient18 = models.CharField(max_length=128)
    strIngredient19 = models.CharField(max_length=128)
    strIngredient20 = models.CharField(max_length=128)
    strMeasure1 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure2 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure3 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure4 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure5 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure6 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure7 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure8 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure9 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure10 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure11 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure12 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure13 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure14 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure15 = models.CharField(max_length=128, blank=True, null=True)
    strMeasure16 = models.CharField(max_length=128)
    strMeasure17 = models.CharField(max_length=128)
    strMeasure18 = models.CharField(max_length=128)
    strMeasure19 = models.CharField(max_length=128)
    strMeasure20 = models.CharField(max_length=128)
    strSource = models.CharField(max_length=128, blank=True, null=True)
    strImageSource = models.CharField(max_length=128)

