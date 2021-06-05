from django.urls import path

from .import views
from .import views

app_name="manageType"
urlpatterns = [
    path('', views.ListView.as_view(), name="list"),
    path('create/', views.TypeCreateView.as_view(), name="create"),
    path('detail/<int:pk>', views.TypeUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', views.TypeDeleteView.as_view(), name="delete"),
]
