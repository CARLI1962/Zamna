from django.db import models

# Create your models here.
class Alacena(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')