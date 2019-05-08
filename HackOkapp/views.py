from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import Video,Child
from .forms import VideoForm,ChildForm
import sys
import argparse
import cv2
import numpy as np
import os
import face_recognition
import glob
from PIL import Image
from matplotlib import cm
from matplotlib import pyplot as plt
import imutils
import re

def PoliceView(request):
    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image1 = face_recognition.load_image_file('media/'+str(Child.objects.last().child_pic))
            list_of_face_encodings1 = face_recognition.face_encodings(image1)
            images = []
            for img in glob.glob("data/*"):
                print(img)
                image2 = face_recognition.load_image_file(img)
                list_of_face_encodings2 = face_recognition.face_encodings(image2)
                if len(list_of_face_encodings2) == 0:
                    continue
                results = face_recognition.compare_faces(list_of_face_encodings1, list_of_face_encodings2)
                print(results[0])
                if results[0] == True:
                    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    url=os.path.join(BASE_DIR, img)
                    sentence = img
                    word = "_"
                    s=-1
                    e=-1
                    for match in re.finditer(word, sentence):
                        if e==-1:
                            e=match.end()
                        else:
                            s=match.start()
                    return render(request, 'result.html',{'text':'Person Found','found':'Person Found','location':sentence[e:s]})
            return render(request, 'result.html',{'text':'Person Not Found','found':'Person Found'})
        else:
            print("Form not valid")
    else:
        form = ChildForm()
    return render(request, 'policeinfo.html', {'form': form})

def facechop(img,location,currentFrame):  
    facedata = "media/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    faces = cascade.detectMultiScale(img)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        sub_face = img[y:y+h, x:x+w]
        file_name = "data/frame" + "_" + location + "_" + str(currentFrame) + ".jpg"
        cv2.imwrite(file_name, sub_face)

def HelperView(request):
    if request.method == "POST":
        print(request.FILES['videofile'])
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            FPS = 10
            cap = cv2.VideoCapture('media/'+str(Video.objects.last().videofile))
            cap.set(cv2.CAP_PROP_FPS, FPS)
            j=cap.get(cv2.CAP_PROP_FPS)
            print(j)
            try:
                if not os.path.exists('data'):
                    os.makedirs('data')
            except OSError:
                print ('Error: Creating directory of data')
            currentFrame = 0
            while(True):
                ret, frame = cap.read()
                if not ret: break
                rotated_frame = imutils.rotate_bound(frame, 90)
                facechop(rotated_frame,request.POST['location'],currentFrame)
                print ('Creating...' + str(currentFrame))
                currentFrame += 1
            cap.release()
            cv2.destroyAllWindows()
            return redirect('home')
        else:
            print("Form not valid")
    else:
        form = VideoForm()
    return render(request, 'helper.html', {'form': form})

def ResultView(request):
    return render(request,"result.html")
