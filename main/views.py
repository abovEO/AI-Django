from fileinput import filename
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from main.camera import MaskDetect, LiveWebCam
from django.shortcuts import render
from .forms import UserForm, CaptureIn
import cv2
from .models import Userinfo, captureDatasets
import os
from cv2 import VideoCapture
from PIL import Image
# Create your views here.

def pageInput(request):
    submitbutton = request.POST.get("submit")
    
    firstname = ''
    links = ''
    # emailvalue=''

    form = UserForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get("first_name")
        links = form.cleaned_data.get("links")
        # emailvalue= form.cleaned_data.get("email")

        reg = Userinfo(id=1, name=firstname, link=links)
        reg.save()
    context = {'form': form, 'firstname': firstname, 'links': links,
               'submitbutton': submitbutton}

    return render(request, 'pageInput.html', context)



# datasets input


def datasetin(request):
    submitbutton = request.POST.get("submit")

    folder = ''
    img = ''
    links = ''
    # emailvalue=''

    form = CaptureIn(request.POST or None)
    if form.is_valid():
        folder = form.cleaned_data.get("folder_name")
        img = form.cleaned_data.get("img_count")
        links = form.cleaned_data.get("capturelinks")

        directory = folder
        imagecount = img
        linkss = Userinfo(link=links)
        linkss.save()
        reg = captureDatasets(id=1, folder_name=folder, images_count=img)
        reg.save()
        feched_link = Userinfo.objects.values_list('link').first()
        realdata = str(feched_link)[2:-3]
        print(realdata)
        linkk = realdata
        
        if directory != 'quite':
            os.mkdir('dataset/'+directory)
        os.makedirs(directory,exist_ok=True)
        
        vs = cv2.VideoCapture(linkk)

        
        filename = len(os.listdir(directory))
        count = 0
        
        while True and count < imagecount:
            filename += 1
            count += 1
            ret, frame = vs.read()
            # im = Image.fromarray(frame, 'RGB')
            # im = im.resize((224, 224))
            if ret == False:
                break
            cv2.imwrite(os.path.join('dataset/'+directory, str(filename) + ".jpg"), frame)

           
        
      


    context = {'form': form, 'folder_name': folder, 'img_count': img, 'capturelinks': links,
               'submitbutton': submitbutton}

    return render(request, 'capturein.html', context)



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def mask_feed(request):
    return StreamingHttpResponse(gen(MaskDetect()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')



def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'home.html')


def devices(request):
    return render(request, 'devices.html')


def camerastreaming(request):
    return render(request, 'camerastreaming.html')


def cameramanagement(request):
    return render(request, 'cameramanagement.html')


def map(request):
    return render(request, 'map.html')

def videoss(request):
    return render(request, 'videoss.html')
