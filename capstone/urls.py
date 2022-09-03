from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("edit/<str:id>", views.edit, name="edit"),
    path("complete/<str:id>", views.complete, name="complete"),
    path("task/<str:id>", views.task, name="task"),
    path("delete/<str:id>", views.delete, name="delete"),
    path("search", views.search, name="search")
]