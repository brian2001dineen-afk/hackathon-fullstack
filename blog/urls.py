from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('createpost/', views.post_create, name='post_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit-comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<int:post_id>/delete-comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<int:post_id>/editpost/', views.post_edit, name='post_edit'),
    path('<int:post_id>/deletepost/', views.post_delete, name='post_delete'),
]
