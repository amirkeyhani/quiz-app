from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=250, null=True)
    option1 = models.CharField(max_length=100, null=True)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, null=True)
    option4 = models.CharField(max_length=100, null=True)
    answer = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.question