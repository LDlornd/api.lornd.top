from django.urls import path, include

from yiqiping import views

urlpatterns = [
    path('login/', views.Login.as_view()),
]