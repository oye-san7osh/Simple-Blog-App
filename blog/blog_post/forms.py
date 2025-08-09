from django import forms
from blog_post.models import Post

class CreatePost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["post_name", "post_detail"]