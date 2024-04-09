from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # ('경로' , 호출할 view 함수),
]