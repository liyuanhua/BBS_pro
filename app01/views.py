from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import BBS
# Create your views here.

def index(request):
    bbs_list = BBS.objects.all()
    return render_to_response('index.html', {"bbs_list": bbs_list})

