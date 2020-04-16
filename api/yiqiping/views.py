from django.core.exceptions import ObjectDoesNotExist
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
        session = request.POST.get("session")
        user = User.objects.get(session=session)
        return_data = []
        if user is null:
            return_data["status"] = -1
            return_data["message"] = "session is invalid!"
        else:
            openid = user.openid
            session_key = user.session_key

    def post(self, request):
        code = request.POST.get("code")
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

class SetInformation(View):
    def post(self, request):
        province = request.POST.get("province")
        city = request.POST.get("city")
        name = request.POST.get("name")
        session = request.POST.get("session")
        return_data = {}
        try:
            user = User.objects.get(session=session)
        except ObjectDoesNotExist:
            return_data["status"] = -1
            return_data["message"] = "session is invalid!"
        else:
            user.province = province
            user.city = city
            user.name = name
            user.save()
            return_data["status"] = 0
            return_data["message"] = "success"
        return JsonResponse(return_data)
