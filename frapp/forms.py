from django import forms
from .models import *


#class SubscribeForm(forms.Form):
  #  email = forms.EmailField()

########################## event add form #############################

class atly_feedback_form(forms.ModelForm):
    class Meta:
        model=atly_feedback
        fields=['name','email','text','message']

class add_work_form(forms.ModelForm):
    class Meta:
        model=add_work
        fields=['name','description','img_link','thumb_link']

class add_blog_form(forms.ModelForm):
    class Meta:
        model=add_blog_table
        fields=['name','type','description','img_link','thumb_link']