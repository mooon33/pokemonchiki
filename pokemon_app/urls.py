from django.urls import path
from . import views

urlpatterns = [
    path('', views.fullpage_view, name='fullpage'),
    path('types/', views.types_view, name='types'),
]