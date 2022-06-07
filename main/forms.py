import cv2,os,urllib.request
import numpy as np
from django import forms


class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    links= forms.CharField(max_length=1000)
    

class CaptureIn(forms.Form):
    folder_name= forms.CharField(max_length=100)
    img_count= forms.IntegerField()
    capturelinks= forms.CharField(max_length=1000)
    

