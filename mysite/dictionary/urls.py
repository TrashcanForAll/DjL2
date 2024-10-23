from django.urls import path
from . import views

app_name = "dictApp"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home),
    path('words_list/', views.wordsList, name="wordsList"),
    path('add_word/', views.addWord, name="addWord"),
]
