# Generated by Django 4.0.3 on 2022-05-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softfactory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealsItems',
            fields=[
                ('strMeal', models.CharField(blank=True, max_length=128, null=True)),
                ('strMealThumb', models.TextField(blank=True, null=True)),
                ('idMeal', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='MealItems',
        ),
    ]
