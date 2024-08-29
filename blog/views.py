from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )




# def post_list(request):
   
#         posts = Post.published.all()  # Fetch all published posts
#         return render(request, 'blog/post/list.html', {'posts': posts})  # Render the template with posts
  


# def post_list(request):
#     try:
#         posts = Post.published.all()
#         return render(request, 'blog/post/list.html', {'posts': posts})
#     except Exception as e:
#         # Debugging output
#         print(f"Error in post_list view: {e}")
#         # Optionally handle the error or log it
#         return render(request, 'blog/post/list.html', {'posts': []})  # Return an empty list or a custom error page






def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )