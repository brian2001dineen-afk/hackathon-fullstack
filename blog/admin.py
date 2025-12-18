from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('id', 'title', 'author', 'created_on', 'approved')
    search_fields = ['title', 'content', 'approved']
    list_filter = ('created_on', 'approved')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'author', 'post', 'created_on', 'approved')
    search_fields = ['body', 'approved']
    list_filter = ('created_on', 'approved')
    summernote_fields = ('body',)
