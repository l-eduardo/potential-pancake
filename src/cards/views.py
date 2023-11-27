from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from cards.forms import CardForm, SharedCardForm
from cards.models import Card, SharedCard
from tasks.models import Task


@login_required()
def list_all(request):
    cards_tasks = {}
    cards = get_cards_for_user(request.user)

    for card in cards:
        tasks = Task.objects.filter(card=card)[:4]
        cards_tasks[card] = tasks

    return render(request, 'cards.html', {'cards_tasks': cards_tasks})


@login_required()
def create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_all')
    elif request.method == "GET":
        form = CardForm()
        return render(request, 'create_card.html', {'form': form})


@login_required()
def delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if card.user_has_permission(request.user, "delete_card"):
        card.delete()
        return redirect('cards:list_all')

    return HttpResponseForbidden("Você não tem permissão para remover este card.")


@login_required()
def share(request):
    if request.method == "POST":
        card_id = request.POST.get('card')
        card = get_object_or_404(Card, id=card_id, owner=request.user)

        if card:
            user_to_share = request.POST.get('shared_with')
            shared_card = SharedCard.objects.filter(card=card, shared_with=user_to_share).first()

            form = SharedCardForm(request.POST, instance=shared_card)
            if form.is_valid():
                form.save()
            return redirect('cards:list_all')

        return HttpResponseForbidden("Você não tem permissão para compartilhar este card.")
    elif request.method == "GET":
        form = SharedCardForm()
        return render(request, 'share_card.html', {'form': form})


@login_required()
def update(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid() and card.user_has_permission(request.user, "change_card"):
            form.save()
            return redirect('cards:list_all')

        return HttpResponseForbidden("Você não tem permissão para atualizar este card.")

    form = CardForm(instance=card)

    return render(request, 'update_card.html', {'form': form})


def get_cards_for_user(user):
    owned_cards = Card.objects.filter(owner=user)

    shared_card_ids = SharedCard.objects.filter(shared_with=user).values_list('card', flat=True)
    shared_cards = Card.objects.filter(pk__in=shared_card_ids)

    cards = list(owned_cards) + list(shared_cards)

    return cards


@login_required()
def find_by_id(request, pk):
    card = get_object_or_404(Card, pk=pk)
    tasks = Task.objects.filter(card=card)
    if card.user_has_permission(request.user, "view_card"):
        return render(request, 'card.html', {
            'card': card,
            'tasks': tasks
        })

    return HttpResponseForbidden("Você não tem permissão para acessar este card.")


@login_required()
def share(request):
    if request.method == "POST":
        form = SharedCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:list_all')
    elif request.method == "GET":
        form = SharedCardForm()
        return render(request, 'share_card.html', {'form': form})