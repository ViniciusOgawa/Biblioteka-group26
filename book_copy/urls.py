from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/copy/", views.CopyView.as_view()),
] 