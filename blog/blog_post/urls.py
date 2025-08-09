from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('lists/', views.blog_lists, name = "blog-list"),
]