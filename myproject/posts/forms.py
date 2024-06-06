from django import forms
from .models import Post

class CreatePosts(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'banner']