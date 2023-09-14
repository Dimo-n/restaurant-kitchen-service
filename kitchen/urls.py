from django.urls import path

from kitchen.views import index, DishTypeListView, DishListView, CookListView

urlpatterns = [
    path("", index,  name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dishes-list"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cooks-list"
    )
]

app_name = "kitchen"
