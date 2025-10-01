from django.urls import path
from . import views
urlpatterns = [
    path("", views.StratingPageView.as_view() , name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SingelPostView.as_view(), name="post-detail-page")
]
