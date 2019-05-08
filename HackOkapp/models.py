from django.db import models

class Child(models.Model):
    name=models.CharField(max_length=256)
    age=models.IntegerField(null=True)
    child_pic = models.ImageField(upload_to = 'HackOkPlease/pic_folder/', default = 'HackOkapp/pic_folder/None/no-img.jpg',null=False)
    child_info=models.TextField(null=True)
    contact=models.CharField(null=True,max_length=256)

class Video(models.Model):
    location = models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
