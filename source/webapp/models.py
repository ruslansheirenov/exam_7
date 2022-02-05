from django.db import models
from django.urls import reverse

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True

class Poll(BaseModel):
    question = models.CharField(max_length=200, null=False, blank=False, verbose_name="Вопрос")

    def get_absolute_url(self):
        return reverse('question_view', kwargs={'pk': self.pk})

    def upper(self):
        return self.question.upper()

    def __str__(self):
        return f"{self.pk}. {self.question}"

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Choice(BaseModel):
    choice = models.TextField(max_length=2000, verbose_name="Ответ")
    question = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE,
                                related_name="choices",
                                verbose_name="Опрос",
                                )

    class Meta:
        db_table = 'choices'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'