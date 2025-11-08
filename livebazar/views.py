from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from dotenv import load_dotenv
import requests
import os

load_dotenv()

TOKEN = os.getenv("TG_API")
CHAT_ID = os.getenv("USER_ID")

def home(request: HttpRequest)->HttpResponse:
    return render(request=request, template_name="index.html")

def support(request:HttpRequest)->HttpResponse:
    if request.method == "POST":
        name = request.POST.get("ism")
        telefon = request.POST.get("telefon")
        message = request.POST.get("xabar")


        user_message = f"👤: {name} \n 📱:{telefon} \n 📩:{message}"


        urls = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": user_message
        }

        requests.post(url=urls, params=payload)

        return render(request=request, template_name="support.html")
    
    return render(request=request, template_name="support.html")


   
