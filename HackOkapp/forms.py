from django import forms
from . models import Child,Video

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ('name','age','contact','child_pic')

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["location", "videofile"]