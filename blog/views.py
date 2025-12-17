from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, UserPostForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1, approved=True)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, post_id):
    """Display an individual :model:`blog.Post`.
    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    try:
        post = Post.objects.get(id=post_id)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        comment_form = CommentForm()
        # ...any other logic for existing posts...
    except Post.DoesNotExist:
        post = None
        comments = []
        comment_count = 0
        comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },)


def post_create(request):
    """
    Create an instance of :model:`post.UserPost`.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``post_create_form``
        An instance of :form:`post.UserPostForm`

    **Template:**

    :template:`post_create.html`
    """
    if request.method == 'POST':
        post_create_form = UserPostForm(request.POST, request.FILES)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted and awaiting approval.')
            return redirect('home')  # Change to your posts list view

    post_create_form = UserPostForm()
    return render(
        request, 'blog/post_create.html',
        {'post_create_form': post_create_form, },)


def comment_edit(request, post_id, comment_id):
    """
    Displays an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    """

    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))


def comment_delete(request, post_id, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))


def post_edit(request, post_id):
    """
    Edit a post.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.

    ``post_edit_form``
        An instance of :form:`post.UserPostForm`

    **Template:**

    :template:`post_edit.html`
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_edit_form = UserPostForm(
            request.POST, request.FILES, instance=post)
        if post_edit_form.is_valid():
            post = post_edit_form.save(commit=False)
            post.approved = False
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post updated and awaiting approval.')
            return redirect('home')
    else:
        post_edit_form = UserPostForm(instance=post)
    return render(request, 'blog/post_edit.html', {
        'post_edit_form': post_edit_form,
        'userpost': post,
    })


def post_delete(request, post_id):
    """
    Delete a post.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    """
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted.')

    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own posts.')
    return redirect('home')