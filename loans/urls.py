from django.urls import path

from . import views

urlpatterns = [
    path("loans/<int:user_id>/<int:book_id>/", views.LoanView.as_view()),
    path("loans/<int:user_id>/history/", views.LoanHistoryView.as_view()),
    path("loans/<int:loan_id>/receive/", views.LoanDetailView.as_view()),
]
