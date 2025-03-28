from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('types/', views.types_view, name='types'),
]