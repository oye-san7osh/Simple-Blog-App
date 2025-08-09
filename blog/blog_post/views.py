from django.shortcuts import render

# Create your views here.
def blog_lists(request):
    return render(request, 'blog_post/blog-lists.html')


