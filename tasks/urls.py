from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("delete/<int:id>", views.delete, name='delete'),
    path("finish/<int:id>", views.finish, name='finish')
]