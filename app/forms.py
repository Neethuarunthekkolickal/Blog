from django import forms
from . models import Post

class MakePost(forms.ModelForm):
    class Meta:
        model=Post
        fields = '__all__'
        labels = {
            'title':'Enter the title',
            'content':"Type Content Here..",
            'image':'Select Image'
        }