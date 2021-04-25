from django.db import models

#Datubāzes modulis jautājumiem
class Question(models.Model):
    q = models.TextField(max_length=800, blank=False, null=False)
    xtraInfo = models.TextField(max_length=2500, default="")
    image = models.CharField(max_length=100)

#Datubāzes modulis iespējām
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    correct = models.BooleanField(default=False)
    choice_text = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return f'{self.id} {self.choice_text} {self.correct}'

#Datubāzes modulis Dalībniekiem
class Member(models.Model):
    username = models.CharField(max_length=50, default="Anonymous user")
    score = models.IntegerField() 
