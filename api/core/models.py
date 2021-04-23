from django.db import models

class Question(models.Model):
    q = models.TextField(max_length=800, blank=False, null=False)
    xtraInfo = models.TextField(max_length=2500, default="")
    image = models.CharField(max_length=100)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    choice_text = models.TextField(max_length=1000, blank=False, null=False)

class Member(models.Model):
    username = models.CharField(max_length=50, default="Anonymous user")
    score = models.IntegerField()
