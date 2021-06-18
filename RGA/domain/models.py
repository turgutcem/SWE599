from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class DomainKnowledge(MPTTModel):

    pass


class Game(models.Model):
    game_name = models.CharField(max_length=100, null=False, default="trial", name="game_name")
    game_tree = models.TextField(name="game_tree")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
