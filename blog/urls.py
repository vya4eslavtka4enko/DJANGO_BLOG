from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name = "starting-page"),
    path("post", views.posts, name = "post-page"),
    path("post/<str:slug>",views.post_detail,name = "post-page-detail") # /post/my-first-post
]