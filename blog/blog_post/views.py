from django.shortcuts import render, redirect
from blog_post.forms import CreatePost
from blog_post.models import Post

# Create your views here.
def blog_lists(request):
    postlists = Post.objects.filter(created_by = request.user).order_by('-post_date')
    return render(request, 'blog_post/blog-lists.html', {"postlist" : postlists})


def blog_detail(request, slug_link):
    postdetail = Post.objects.get(slug_link = slug_link)
    return render(request, 'blog_post/blog-detail.html', {"postdetail" : postdetail})


def create_blog(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.created_by = request.user
            post.save()
            return redirect('blog:blog-list')
    else:
        form = CreatePost()
    return render(request, 'blog_post/create-blog.html', {"form" : form})


def update_blog(request, slug_link):
    post = Post.objects.get(slug_link = slug_link)
    
    if request.method == "POST":
        form = CreatePost(request.POST, instance = post)
        
        if form.is_valid():
            form.save()
            return redirect('blog:blog-detail', slug_link = post.slug_link)
    
    else:
        form = CreatePost(instance = post)
    return render(request, 'blog_post/update-blog.html', {"form" : form})


def delete_blog(request, slug_link):
    post = Post.objects.get(slug_link = slug_link)
    
    if request.method == "POST":
        post.delete()
        return redirect("blog:blog-list")

    return render(request, 'blog_post/delete-blog.html', {"post" : post})