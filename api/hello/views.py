from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Hello(View):
    def get(self, request):
        return HttpResponse("hello,World!")

    def post(self, request):
        pass
