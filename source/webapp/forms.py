from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        question = cleaned_data['question']
        if len(question) < 10:
            self.add_error('question', ValidationError(
                f"Значение не может быть менее 10 символов, {question} не подходит"))
        return cleaned_data

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")

class PollDeleteForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("question",)

    def clean_title(self):
        if self.instance.title != self.cleaned_data.get("question"):
            raise ValidationError("Название вопроса не соответствует")
        return self.cleaned_data.get("question")