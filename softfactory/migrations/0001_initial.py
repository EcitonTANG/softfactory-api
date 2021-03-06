# Generated by Django 4.0.3 on 2022-05-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItems',
            fields=[
                ('idCategory', models.IntegerField(primary_key=True, serialize=False)),
                ('strCategory', models.CharField(blank=True, max_length=128, null=True)),
                ('strCategoryThumb', models.TextField(blank=True, null=True)),
                ('strCategoryDescription', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealItems',
            fields=[
                ('strMeal', models.CharField(blank=True, max_length=128, null=True)),
                ('idMeal', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('idMeal', models.IntegerField(primary_key=True, serialize=False)),
                ('strMeal', models.CharField(blank=True, max_length=128, null=True)),
                ('strCategory', models.CharField(blank=True, max_length=128, null=True)),
                ('strInstruction', models.TextField(blank=True, null=True)),
                ('strMealThumb', models.TextField(blank=True, null=True)),
                ('strTags', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient1', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient2', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient3', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient4', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient5', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient6', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient7', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient8', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient9', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient10', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient11', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient12', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient13', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient14', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient15', models.CharField(blank=True, max_length=128, null=True)),
                ('strIngredient16', models.CharField(max_length=128)),
                ('strIngredient17', models.CharField(max_length=128)),
                ('strIngredient18', models.CharField(max_length=128)),
                ('strIngredient19', models.CharField(max_length=128)),
                ('strIngredient20', models.CharField(max_length=128)),
                ('strMeasure1', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure2', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure3', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure4', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure5', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure6', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure7', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure8', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure9', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure10', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure11', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure12', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure13', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure14', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure15', models.CharField(blank=True, max_length=128, null=True)),
                ('strMeasure16', models.CharField(max_length=128)),
                ('strMeasure17', models.CharField(max_length=128)),
                ('strMeasure18', models.CharField(max_length=128)),
                ('strMeasure19', models.CharField(max_length=128)),
                ('strMeasure20', models.CharField(max_length=128)),
                ('strSource', models.CharField(blank=True, max_length=128, null=True)),
                ('strImageSource', models.CharField(max_length=128)),
            ],
        ),
    ]
