from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.middleware.csrf import get_token

# Create your views here.
from django.views import View


class Hello(View):
    def get(self, request):
        a = get_token(request)
        return HttpResponse("hello,123!")

    def post(self, request):
        a = request.POST.get('a')
        b = request.POST.get('b')
        return JsonResponse(data={'c': a + b})
