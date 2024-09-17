from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('portao', views.portao),
    path('sala', views.sala),
    path('quarto', views.quarto),
]
