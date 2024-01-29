from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("post", views.AllPostsView.as_view(), name = "post-page"),
    path("post/<str:slug>",views.SingPostView.as_view(),name = "post-page-detail") # /post/my-first-post
]