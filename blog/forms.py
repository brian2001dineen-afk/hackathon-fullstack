from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Creates a form for :model:`blog.Comment` to create comments
    """
    class Meta:
        model = Comment
        fields = ('body',)


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'featured_image', 'content', 'status', 'excerpt']
