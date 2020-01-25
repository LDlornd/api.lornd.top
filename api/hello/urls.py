from django.urls import path, include

from hello import views

urlpatterns = [
    path('', views.Hello.as_view()),
]