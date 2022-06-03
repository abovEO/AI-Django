# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.http.response import StreamingHttpResponse



#@login_required(login_url="/login/")

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

        html_template = loader.get_template('home/cameradtreaming.html' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def video_feedd(request):
    return StreamingHttpResponse(gen(VideoCameraa()),
                    content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
    return StreamingHttpResponse(gen(IPWebCam()),
                    content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
    return StreamingHttpResponse(gen(MaskDetect()),
                    content_type='multipart/x-mixed-replace; boundary=frame')
                    
def livecam_feed(request):
    return StreamingHttpResponse(gen(LiveWebCam()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def web_feed(request):
    return StreamingHttpResponse(gen(mainn()),
                    content_type='multipart/x-mixed-replace; boundary=frame')


def face_feed(request):
    return StreamingHttpResponse(gen(non_max_suppression_fast()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def human_feed(request):
    return StreamingHttpResponse(gen(CentroidTracker()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

'''
def index(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'home.html')

def devices(request):
    return render(request,'devices.html')
'''
def camerastreaming(request):
    return render(request,'camerastreaming.html')

def cameramanagement(request):
    return render(request,'cameramanagement.html')


def map(request):
    return render(request,'map.html')

