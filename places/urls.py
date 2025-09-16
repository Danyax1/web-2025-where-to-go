from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('', views.index, name='index'),
    path("list/", views.places_list, name="places_list"),
    path("add/", views.add_place, name="add_place"),
    path("place/<int:pk>/", views.place_detail, name="place_detail"),
    path("random-json/", views.random_place_json, name="random_place_json"),

]
