from django.urls import path
from django.views.generic import RedirectView

from webapp.views.poll import (
    PollCreateView,
    PollView,
    PollUpdateView,
    PollDeleteView,
    IndexView)

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('questions/', RedirectView.as_view(pattern_name="index")),
    path('question/add/', PollCreateView.as_view(), name="question_add"),
    path('question/<int:pk>/', PollView.as_view(template_name="poll/view.html"), name="question_view"),
    path('question/<int:pk>/update/', PollUpdateView.as_view(), name="question_update_view"),
    path('question/<int:pk>/delete/', PollDeleteView.as_view(), name="question_delete_view"),
]