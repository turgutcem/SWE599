from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def play_view(request):
    return render(request, "domain/play.html")


@login_required
def create_view(request):
    return render(request, "domain/create.html")
