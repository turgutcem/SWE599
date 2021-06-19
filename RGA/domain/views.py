from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Game, DomainKnowledge


# Create your views here.


@login_required
def play_view(request):
    other_games = Game.objects.exclude(created_by=request.user)
    your_games = Game.objects.filter(created_by=request.user)
    context = {'other_games': other_games, 'your_games': your_games}

    return render(request, "domain/play.html", context=context)


@login_required
def play_game_view(request, pk):
    game = Game.objects.filter(pk=pk).last()
    dk = DomainKnowledge()
    dk.game = game
    dk.parent = None
    dk.type = 'INTRO'
    dk.save()
    print(game.game)
    return render(request, "domain/play_game.html")


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
        return JsonResponse({"success": True}, status=200)
    except:
        return JsonResponse({"success": False}, status=400)
