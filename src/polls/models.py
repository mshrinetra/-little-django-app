import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # Define how a column (was_published_recently) displays in admin view
    # Note it is in class but after and out of method
    was_published_recently.admin_order_field = 'pub_date'  # sort as pub_date
    was_published_recently.boolean = True  # tell the value is boolian
    was_published_recently.short_description = 'Published recently?'  # name to display


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
