from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from cards.forms import CardForm, SharedCardForm
from cards.models import Card


@login_required
def list_all(request):
    cards = get_list_or_404(Card)
    return render(request, 'cards.html', {'cards': cards})


@login_required
def create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_all')
    elif request.method == "GET":
        form = CardForm()
        return render(request, 'create_card.html', {'form': form})


@login_required
def delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('cards:list_all')


@login_required
def update(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('cards:find_by_id', card.id)

    form = CardForm(instance=card)

    return render(request, 'update_card.html', {'form': form})


@login_required
def find_by_id(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'card.html', {'card': card})


@login_required
def share(request):
    if request.method == "POST":
        form = SharedCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_all')
    elif request.method == "GET":
        form = SharedCardForm()
        return render(request, 'share_card.html', {'form': form})
