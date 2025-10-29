from django.db import models
import random

class Question(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

    def get_shuffled_options(self):
        """Return a shuffled list of related options each call."""
        opts = list(self.options.all())
        random.shuffle(opts)
        return opts

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'correct' if self.is_correct else 'wrong'})"
