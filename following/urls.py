from django.urls import path
from . import views


urlpatterns = [
    path("users/<int:book_id>/follow/", views.FollowView.as_view()),
]
