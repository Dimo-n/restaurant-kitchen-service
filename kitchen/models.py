from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes"
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.name}, {self.price} ({self.dish_type.name})"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["last_name"]

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.username})"
