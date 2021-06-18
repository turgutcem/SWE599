from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Game


# Create your views here.


@login_required
def play_view(request):
    return render(request, "domain/play.html")


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
        game.save()
        return JsonResponse({"success": True}, status=200)
    except:
        return JsonResponse({"success": False}, status=400)
