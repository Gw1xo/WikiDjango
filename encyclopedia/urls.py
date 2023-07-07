from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.view_page, name="article"),
    path("add/", views.add_article, name="add"),
    path("wiki/<str:title>/edit", views.edit_article, name="edit"),
    path("random/", views.random_page, name='random')
]
