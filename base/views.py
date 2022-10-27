from base64 import decode
import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
import json
from forms.forms import  Saveimgform
import pandas as pd
import os
import requests

from django.utils.html import format_html

from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from  bs4 import BeautifulSoup
# from rest_framework.generics import 
# from forms.forms
# Create your views here.


from django.http import HttpResponse


# class  serialise_(Serializer):
#     val =Serializer.ch

@api_view(["get","post"])
def home(req):
    section = None

    if req.method =="POST":
        
        post_ = json.loads(json.dumps(req.data))["val"]
       
        
       
        url = f"https://tiktokhashtags.com/hashtag/{post_}/"
        tradingeconomics = requests.get(url).text


        soup = BeautifulSoup(tradingeconomics, "lxml")
        section_ = soup.find("table", class_="table table-bordered")
        section =section_ and format_html( str(section_) )
        print(str(section))



      

        # print(post_)
        
  
    return render(req,"index.html",{"post":section})





