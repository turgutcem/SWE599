from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Game(models.Model):
    game_name = models.CharField(max_length=100, null=False, default="trial", name="game_name")
    game_tree = models.TextField(name="game_tree")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class DomainKnowledge(MPTTModel):
    gamekey = models.IntegerField(null=False)
    quest_type = models.CharField(max_length=100)
    content = models.TextField()
    evaluation = models.CharField(max_length=250, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False, related_name="game_related")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, related_name="children")


class Results(models.Model):
    playid = models.IntegerField(blank=True, default=-1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domainknowledge_pk = models.IntegerField(default=-1)
