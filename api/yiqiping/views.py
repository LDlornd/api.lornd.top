from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views import View
from yiqiping.models import User
import requests, json

class Login(View):
    def __init__(self):
        self.appid = "wxbd16949500a303a3"
        self.appsecret = "f4079c3335530c7f3ab3e1209d51c5e0"

    def get(self, request):
        appid = "wxbd16949500a303a3"
        appsecret = "f4079c3335530c7f3ab3e1209d51c5e0"
        data = {
            "hello": "hello",
        }
        return JsonResponse(data)

    def post(self, request):
        print(request.POST)
        code = request.POST.get("code")
        print(code)
        url = "https://api.weixin.qq.com/sns/jscode2session"
        data = {
            "appid": self.appid,
            "secret": self.appsecret,
            "js_code": code,
            "grant_type": "authorization_code",
        }
        response = requests.get(url=url, params=data)
        data = json.loads(response.text)
        return_data = {}
        if data.get("errcode"):
            return_data["staus"] = -1
            return_data["message"] = data["errmsg"]
        else:
            user = User()
            user.session_key = data["session_key"]
            user.openid = data["openid"]
            if not request.session.session_key:
                request.session.create()
            user.session = request.session.session_key
            user.save()
            return_data["status"] = 0
            return_data["session"] = user.session
        return JsonResponse(return_data)
