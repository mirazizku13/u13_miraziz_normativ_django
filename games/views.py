from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Game
from .forms import GameModelForm


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'games/game_detail.html', {'game': game})


def game_create(request):
    if request.method == 'POST':
        form = GameModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('games:game_list')
    else:
        form = GameModelForm()
    return render(request, 'games/game_form.html', {'form': form})


def game_update(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        form = GameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:game_list')
    else:
        form = GameModelForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

def game_delete(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('games:game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})