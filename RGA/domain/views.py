from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Game, DomainKnowledge
import json


# Create your views here.


@login_required
def play_view(request):
    other_games = Game.objects.exclude(created_by=request.user)
    your_games = Game.objects.filter(created_by=request.user)
    context = {'other_games': other_games, 'your_games': your_games}

    return render(request, "domain/play.html", context=context)


@login_required
def play_game_view(request, pk):
    game = Game()
    game = Game.objects.filter(pk=pk).last()
    domainknowledge = DomainKnowledge()
    domainknowledge = DomainKnowledge.objects.filter(game=game)
    context = {"dk": domainknowledge}
    return render(request, "domain/play_game.html", context=context)


@login_required
def create_view(request):
    return render(request, "domain/create.html")


@login_required
@require_POST
def create_game(request):
    try:
        game = Game()
        game.game_name = request.POST.get("gamename")
        game.game_tree = request.POST.get("gt")
        game.created_by = request.user
        game.validation = False

        game.save()
        save(game.pk)
        return JsonResponse({"success": True}, status=200)
    except:
        return JsonResponse({"success": False}, status=400)


def save(pk):
    game = Game.objects.filter(pk=pk).last()
    game_tree_json = game.game_tree
    a = json.loads(game_tree_json)
    for element in a['nodeDataArray']:
        if ('category', 'Recycle') in element.items():
            continue
        dk = DomainKnowledge()
        dk.game = game
        dk.gamekey = element['key']

        if 'BOT_Q' in element['text']:

            dk.content = element['text'].split('BOT_Q')[1]
            dk.quest_type = 'BOT_Q'

        elif 'INTRO' in element['text']:

            dk.quest_type = 'INTRO'
            dk.content = element['text'].split('INTRO')[1]
        elif 'HUM_Q' and 'EVAL' in element['text']:

            dk.quest_type = 'HUM_Q'
            dk.evaluation = element['text'].split('HUM_Q')[1].split('EVAL')[1]
            dk.content = element['text'].split('EVAL')[0].split('HUM_Q')[1]
        elif 'END' in element['text']:

            dk.quest_type = 'END'
            dk.content = element['text'].split('END')[1]

        else:

            return JsonResponse({"success": False}, status=400)

        dk.save()

    for helement in a['linkDataArray']:
        parentz = DomainKnowledge.objects.filter(game=game, gamekey=int(helement['from'])).last()
        childrenz = DomainKnowledge.objects.filter(game=game, gamekey=int(helement['to'])).update(parent=parentz)

    return JsonResponse({"success": True}, status=200)
