from django.shortcuts import redirect, render, get_object_or_404

from cards.forms import CardForm
from cards.models import Card


def list_cards(request):
    cards = Card.objects.all()
    return render(request, 'cards.html', {'cards': cards})

def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_cards')
    elif request.method == "GET":
        form = CardForm()
        return render(request, 'create_card.html', {'form': form})

def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('cards:list_cards')

def update_card(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('cards:find_card_by_id', card.id)

    form = CardForm(instance=card)

    return render(request, 'update_card.html', {'form': form})

def find_card_by_id(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'card.html', {'card': card})
