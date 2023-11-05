from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "tierlist/create-default",
        views.create_default_tierlist,
        name="tierlist-create-default",
    ),
    path("tierlist/<int:pk>", views.details, name="tierlist-details"),
    path("upload-image/<int:pk>", views.upload_image, name="upload-image"),
    path("dropped", views.dropped, name="dropped"),
    path(
        "tieriem/delete/<int:pk>",
        views.delete_tier_item,
        name="delete-tieritem",
    ),
]
