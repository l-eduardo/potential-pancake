from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from cards.forms import CardForm
from cards.models import Card


def list_all(request):
    cards = get_list_or_404(Card)
    return render(request, 'cards.html', {'cards': cards})


def create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_all')
    elif request.method == "GET":
        form = CardForm()
        return render(request, 'create_card.html', {'form': form})


def delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('cards:list_all')


def update(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('cards:find_by_id', card.id)

    form = CardForm(instance=card)

    return render(request, 'update_card.html', {'form': form})


def find_by_id(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'card.html', {'card': card})
