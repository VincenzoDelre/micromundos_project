from django.urls import path
from . import views

urlpatterns = [
    part('',views.index, name='index')
]
