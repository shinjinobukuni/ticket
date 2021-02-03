from django.urls import path

from .import views

app_name="header"
urlpatterns = [
    path('', views.ListView.as_view(), name="list"),

]
