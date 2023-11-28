from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from cards.forms import CardForm, SharedCardForm
from cards.models import Card, SharedCard
from tasks.models import Task


@login_required
def list_all(request):
    """
    Lista todos os cards associados ao usuário logado, exibindo até 4 tarefas por card.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        HttpResponse: Renderiza a página 'cards.html' com os cards e tarefas associados.
    """
    cards_tasks_permissions = {}

    cards = get_cards_for_user(request.user)

    for card in cards:
        tasks = Task.objects.filter(card=card)[:4]
        cards_tasks_permissions[card] = [tasks, card.user_has_edit_permissions(request.user), card.user_is_owner(request.user)]

    return render(request, 'cards.html', {'cards_tasks_permissions': cards_tasks_permissions})


@login_required
def create(request):
    """
    Cria um novo card associado ao usuário logado.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        HttpResponse: Redireciona para a página 'cards:list_all' após a criação bem-sucedida.
        HttpResponseForbidden: Retorna uma resposta proibida se o usuário não tiver permissão.
    """
    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid() and caller_is_owner(request):
            form.save()
            return redirect('cards:list_all')

        return HttpResponseForbidden('YOU SHALL NOT PASS!')
    elif request.method == 'GET':
        form = CardForm()
        form.fields["owner"].initial = request.user.id
        return render(request, 'create_card.html', {'form': form})


@login_required
def delete(request, pk):
    """
    Exclui um card específico associado ao usuário logado.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária (ID) do card a ser excluído.

    Returns:
        HttpResponse: Redireciona para a página 'cards:list_all' após a exclusão bem-sucedida.
        HttpResponseForbidden: Retorna uma resposta proibida se o usuário não tiver permissão.
    """
    card = Card.objects.get(pk=pk)
    if card.user_is_owner(request.user):
        card.delete()
        return redirect('cards:list_all')

    return HttpResponseForbidden('YOU SHALL NOT PASS!')


@login_required
def update(request, pk):
    """
    Atualiza um card específico associado ao usuário logado.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária (ID) do card a ser atualizado.

    Returns:
        HttpResponse: Redireciona para a página 'cards:list_all' após a atualização bem-sucedida.
        HttpResponseForbidden: Retorna uma resposta proibida se o usuário não tiver permissão.
    """
    card = Card.objects.get(pk=pk)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid() and card.user_is_owner(request.user):
            form.save()
            return redirect('cards:list_all')

        return HttpResponseForbidden('YOU SHALL NOT PASS!')

    form = CardForm(instance=card)

    return render(request, 'update_card.html', {'form': form})


@login_required
def find_by_id(request, pk):
    """
    Exibe informações detalhadas sobre um card específico associado ao usuário logado ou se o usuário
    tiver permissão para acessá-lo.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária (ID) do card a ser exibido.

    Returns:
        HttpResponse: Renderiza a página 'card.html' com informações detalhadas sobre o card e tarefas associadas.
        HttpResponseForbidden: Retorna uma resposta proibida se o usuário não tiver permissão.
    """

    card = Card.objects.get(pk=pk)
    tasks = Task.objects.filter(card=card)
    if card.user_has_permission(request.user, 'view_card'):
        return render(request, 'card.html', {
            'card': card,
            'tasks': tasks,
            'has_edit_permission': card.user_has_edit_permissions(request.user),
            'is_owner': card.user_is_owner(request.user),
        })

    return HttpResponseForbidden('YOU SHALL NOT PASS!')


@login_required
def share(request):
    """
    Compartilha um card específico com outro usuário.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        HttpResponse: Redireciona para a página 'cards:list_all' após o compartilhamento bem-sucedido.
        HttpResponseForbidden: Retorna uma resposta proibida se o usuário não tiver permissão.
    """
    if request.method == 'POST':
        card_id = request.POST.get('card')
        card = Card.objects.get(pk=card_id)
        shared_with_id = request.POST.get('shared_with')
        shared_with = User.objects.get(pk=shared_with_id)
        shared_card = SharedCard.objects.filter(card=card, shared_with=shared_with).first()
        form = SharedCardForm(request.POST, instance=shared_card)

        if request.user == shared_with:
            return redirect('cards:list_all')

        if form.is_valid() and card.user_is_owner(request.user):
            form.save()
            messages.success(request, 'Successful sharing!')
            return redirect('cards:list_all')


        return HttpResponseForbidden('YOU SHALL NOT PASS!')
    elif request.method == 'GET':
        form = SharedCardForm()
        return render(request, 'share_card.html', {'form': form})
   

def caller_is_owner(request):
    """
    Verifica se o usuário que fez a chamada é o proprietário do card. Usado quando o card
    ainda não existe na base de dados.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        bool: True se o usuário que fez a chamada for o proprietário, False caso contrário.
    """
    owner_id = request.POST.get('owner')
    owner = User.objects.get(id=owner_id)
    return request.user == owner


def get_cards_for_user(user):
    """
    Obtém todos os cards associados a um determinado usuário.

    Args:
        user (User): O objeto de usuário Django.

    Returns:
        list: Uma lista de objetos Card associados ao usuário, incluindo os cards de propriedade e compartilhados.
    """
    owned_cards = Card.objects.filter(owner=user)

    shared_card_ids = SharedCard.objects.filter(shared_with=user).values_list('card', flat=True)
    shared_cards = Card.objects.filter(pk__in=shared_card_ids)

    cards = list(owned_cards) + list(shared_cards)

    return cards

@login_required
def list_shared_card_users(request, pk):
    card = Card.objects.get(pk=pk)
    shared_cards = SharedCard.objects.filter(card=card)

    return render(request, 'list_shared_card_users.html', {
        'shared_cards': list(shared_cards),
        'card': card
    })


@login_required
def remove_share(request, pk):
    shared_card = SharedCard.objects.get(pk=pk)

    if shared_card.card.user_is_owner(request.user):
        shared_card.delete()
        return redirect('cards:list_shared_card_users', shared_card.card.id)

    return HttpResponseForbidden("Você não tem permissão para remover o compartilhamento deste card.")


@login_required
def update_share(request, pk):
    shared_card = SharedCard.objects.get(pk=pk)

    if request.method == 'POST':
        form = SharedCardForm(request.POST, instance=shared_card)
        if shared_card and shared_card.card.user_is_owner(request.user) and form.is_valid():
            form.save()
            return redirect('cards:list_shared_card_users', shared_card.card.id)

        return HttpResponseForbidden("Você não tem permissão para atualizar o compartilhamento deste card.")

    form = SharedCardForm(instance=shared_card)
    return render(request, 'update_shared_card.html', {'form': form, 'shared_card_id': shared_card.id})


@login_required()
def share_to_card(request, pk):
    if request.method == "GET":
        form = SharedCardForm()
        form.fields["card"].initial = pk
        return render(request, 'share_card.html', {'form': form})
