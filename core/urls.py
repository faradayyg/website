from django.urls import path

from core import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path(
        "posts/<int:pk>/<str:slug>", views.PostDetailView.as_view(), name="post_detail"
    ),
]
