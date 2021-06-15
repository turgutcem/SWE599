from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class DomainKnowledge(models.Model):
    question = models.TextField()
    pass


class Game(models.Model):
    domain_knowledge = models.ForeignKey(DomainKnowledge,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
