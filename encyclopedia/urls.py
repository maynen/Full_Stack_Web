from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("create_post", views.create_post, name="create_post"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("wiki/<str:title>", views.page, name="page"),
]
