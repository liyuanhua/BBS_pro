from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import BBS
from django_comments.models import Comment
# Create your views here.

def index(request):
    bbs_list = BBS.objects.all()
    return render_to_response('index.html', {"bbs_list": bbs_list})

def bbs_detail(request, bbs_id):
    bbs_obj = BBS.objects.get(id=bbs_id)

    return render_to_response('bbs_detail.html', {"bbs_obj": bbs_obj})

def sub_comment(request):
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')

    # Write comment to DB
    # Be careful about the names of the following parameters.
    # Check django.contrib.contenttypes.models source code if necessary.
    Comment.objects.create(
          content_type_id = 8,
          object_pk = bbs_id,   # Not object_id which is very confusing
          site_id = 1,
          user = request.user,
          comment = comment,
          ip_address="",

    )

    return HttpResponseRedirect('/bbs/detail/%s'%bbs_id)