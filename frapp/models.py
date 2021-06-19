from django.db import models

# Create your models here.


######################### atly feedback #############
class atly_feedback(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

######################### add work #############
class add_work(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    img_link=models.CharField(max_length=1000)
    thumb_link = models.CharField(max_length=1000)


class add_blog_table(models.Model):
    name=models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    img_link=models.CharField(max_length=1000)
    thumb_link = models.CharField(max_length=1000)
