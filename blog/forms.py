from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Creates a form for :model:`blog.Comment` to create comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
