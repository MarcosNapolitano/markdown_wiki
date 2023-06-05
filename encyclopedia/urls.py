from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:boolean>", views.index, name="index2"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("w/query", views.search, name="search"),
    path("w/newpage", views.addPage, name="newpage"),
    path("wiki/<str:title>/editpage/", views.editPage, name="editpage")



]
