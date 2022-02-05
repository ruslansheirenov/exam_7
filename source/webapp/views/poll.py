from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, PollDeleteForm
from webapp.models import Poll


class IndexView(SearchView):
    model = Poll
    context_object_name = "questions"
    template_name = "questions/index.html"
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ["question__icontains"]


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "questions/create.html"


class PollView(DetailView):
    template_name = 'questions/view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = self.object.question.order_by("-created_at")
        context['questions'] = questions
        return context


class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = "questions/update.html"
    model = Poll


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "questions/delete.html"
    success_url = reverse_lazy('index')
    form_class = PollDeleteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs