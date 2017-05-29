# coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf import settings
from django.db.models import F, Q, Count
from django.db import transaction
from datetime import date, datetime
from django.utils import timezone
import time
import csv
import json
import urllib

from .models import *
from formapp.api import *



def index(request):
    return render(request, 'form_gaode.html')

def create(request):
    if request.method != 'POST':
        return HttpResponse(u"NotPermittedError: please use POST!")
    temp = request.body.split('&')
    args = json.loads(temp[0])
    #for (k,v) in data.items():
    #    print k
    #    print v
    #args = QueryDict(data)
    #args={}
    #for i in range(len(temp)):
    #    print temp[i]
    #    args[temp[i].split('=')[0]]=urllib.unquote(temp[i].split('=')[1])
    #data = urllib.urlencode(json.loads(request.body))
    #args = QueryDict(data)

    #args = request.POST
    ip = request.META['REMOTE_ADDR']
    post_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = args['name']
    placeRadio = args['placeRadio']
    placetyped = args['placetyped']
    beforeAction = args['beforeAction']
    jacket = args['jacket']
    trousers = args['trousers']
    temperature = args['temperature']
    confortable = args['confortable']
    totalconf = args['totalconf']
    beats = args['beats']
    lon = args['lon']
    lat = args['lat']
    
    #print name
    #print placetyped

    post_form = Wenjuan(ip=ip, post_time=post_time, name=name, placeRadio=placeRadio, placetyped=placetyped,
            beforeAction=beforeAction, jacket=jacket, trousers=trousers, temperature=temperature,
            confortable=confortable, totalconf=totalconf, beats=beats, lon=lon, lat=lat)
    post_form.save()

    return HttpResponse(u'感谢您提交问卷!')

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachement; filename="wenjuan.csv"'

    writer = csv.writer(response)
    writer.writerow(['ip','post_time','name','placeRadio','placetyped','beforeAction','jacket','trousers','temperature','confortable','totalconf','beats','lat','lon'])
    will_be_writen = get_wenjuan()
    for i in range(len(will_be_writen)):
        writer.writerow(will_be_writen[i])
    return response

def get_wenjuan():
    query = Wenjuan.objects.all()
    all_values = ('ip','post_time','name','placeRadio','placetyped','beforeAction','jacket','trousers','temperature','confortable','totalconf','beats','lat','lon')
    query = query.values_list(*all_values)
    results = map(list, query)
    return results
