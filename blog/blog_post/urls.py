from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('lists/', views.blog_lists, name = "blog-list"),
    path('detail/<slug:slug_link>', views.blog_detail, name = "blog-detail"),
    path('create/', views.create_blog, name = "create-blog"),
    path('update/<slug:slug_link>', views.update_blog, name = "update-blog"),
    path('delete/<slug:slug_link>', views.delete_blog, name = "delete-blog"),
]