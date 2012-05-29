# -*- coding: utf-8 -*-
# Create your views here.
from django.template import Context, loader
from django.http import  HttpResponse
from models import Punchcollection,Punch,User
from django.http import Http404
from django.shortcuts import render_to_response
import tweepy

def users(request):
    users_list = User.objects.all()
    t = loader.get_template('punch/users.html')
    c = Context({
        'users_list': users_list,
    })
    return HttpResponse(t.render(c))
    #return HttpResponse("this is the in


def CollectionsByUser(request,user_id):
    user = User.objects.get(pk=user_id)
    collection_list =  user.punchcollection_set.all()
     # collection_list = Punchcollection.objects.all()
    t = loader.get_template('punch/index.html')
    c = Context({
        'collection_list': collection_list,
    })
    return HttpResponse(t.render(c))

def getAllPunches(request):
    allPunches = Punch.objects.all()
    sortedPunches = sorted(allPunches,key=lambda punch: punch.funny_count)
    return render_to_response('punch/home.html', {'punchList': sortedPunches})

    

def index(request):
    collection_list = Punchcollection.objects.all()
    t = loader.get_template('punch/index.html')
    c = Context({
        'collection_list': collection_list,
    })
    return HttpResponse(t.render(c))
    #return HttpResponse("this is the index page for collections")
#def detail(request,collection_id):
 #   return HttpResponse("this is punchcollection number %s" %collection_id)


def detail(request, collection_id):
    try:
        collection = Punchcollection.objects.get(pk=collection_id)
    except Punchcollection.DoesNotExist:
        raise Http404
    return render_to_response('punch/detail.html', {'collection': collection})

from django.utils import simplejson
from django.shortcuts import  get_object_or_404

def follow(request, user_id, follow_id):
    currentUser = User.objects.get(pk=user_id)
    followUser = User.objects.get(pk=follow_id)  
    
    currentUser.following.add(followUser)
    followUser.followers.add(currentUser)

def make_boo(request, punch_id):   
    message = {"booCount": "","id": ""}

    if request.is_ajax():
        punch = get_object_or_404(Punch, id=punch_id)
        punch.boo_count += 1
        punch.save()
        message['booCount'] = punch.boo_count
        message['id'] = punch_id
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')

def make_funny(request, punch_id):   
    message = {"funnyCount": "","id": ""}

    if request.is_ajax():
        punch = get_object_or_404(Punch, id=punch_id)
        punch.funny_count = punch.funny_count +1
        punch.save()
        message['funnyCount'] = punch.funny_count
        message['id'] = punch_id
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')