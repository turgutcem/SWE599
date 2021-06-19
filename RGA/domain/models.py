from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.


class Game(models.Model):
    validation = models.BooleanField()
    game_name = models.CharField(max_length=100, null=False, default="trial", name="game_name")
    game_tree = models.TextField(name="game_tree")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class DomainKnowledge(MPTTModel):
    INTRO = 'INTRO'
    BOT_Q = 'BOT_Q'
    ANSWER = 'ANSWER'
    END = 'END'
    CHOICES = ((INTRO, INTRO), (BOT_Q, BOT_Q), (ANSWER, ANSWER), (END, END))

    type = models.CharField(max_length=100, choices=CHOICES, name="type_of")
    content = models.TextField()
    evaluation = models.CharField(max_length=250, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False, related_name="game")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")
