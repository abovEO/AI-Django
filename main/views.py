'''
from django.shortcuts import render,HttpResponse,redirect
from django.http.response import StreamingHttpResponse
from main.camera import VideoCamera, IPWebCam, MaskDetect, LiveWebCam

# Create your view def createDataset(self):
        
        self.feched_link = Userinfo.objects.values_list('link').first()
        self.realdata = str(self.feched_link)[2:-3]
        print(self.realdata)
        dlink = self.realdata
        self.vs = VideoCapture(dlink).start()
         def createDataset(self):
        
        self.feched_link = Userinfo.objects.values_list('link').first()
        self.realdata = str(self.feched_link)[2:-3]
        print(self.realdata)
        dlink = self.realdata
        self.vs = VideoCapture(dlink).start()
        s here.

#main file rendering

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):

	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def livecam_feed(request):
	return StreamingHttpResponse(gen(main()),
					content_type='multipart/x-mixed-replace; boundary=frame')			

def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')
				

def webcam_feed(request):
	return StreamingHttpResponse(gen(CentroidTracker()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def video_feedd(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(CentroidTracker()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
	return StreamingHttpResponse(gen(main()),
					content_type='multipart/x-mixed-replace; boundary=frame')
					
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')				



def index(request):
	return render(request,'home.html')

def login(request):
	return render(request,'login.html')
	'''
from fileinput import filename
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from main.camera import MaskDetect

from django.shortcuts import render
from .forms import UserForm, CaptureIn
import cv2
from .models import Userinfo
import os
from cv2 import VideoCapture
from PIL import Image
# Create your views here.

'''
def index(request):
	return render(request, 'main/home.html')
'''
# def new_page(request):
# 	data = request.GET['fulltextarea']
# 	l = data
# 	return render(request, 'newpage.html', {'data':data})


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
    # emailvalue=''

    form = CaptureIn(request.POST or None)
    if form.is_valid():
        folder = form.cleaned_data.get("folder_name")
        img = form.cleaned_data.get("img_count")
        # emailvalue= form.cleaned_data.get("email")
        directory = folder
        imagecount = img
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
            _, frame = vs.read()
            im = Image.fromarray(frame, 'RGB')
            im = im.resize((224, 224))
            im.save(os.path.join(directory, str(filename) + ".jpg"), "JPEG")

            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        vs.release()
        cv2.destroyAllWindows()
        
      


    context = {'form': form, 'folder_name': folder, 'img_count': img,
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
