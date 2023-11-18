from django.urls import path

from cards.views import create_card, list_cards, delete_card, update_card, find_card_by_id

app_name = 'cards'

urlpatterns = [
    path("create-card/", create_card, name="create_card"),
    path("cards/", list_cards, name="list_cards"),
    path("cards/<int:pk>/", find_card_by_id, name="find_card_by_id"),
    path("delete-card/<int:pk>/", delete_card, name="delete_card"),
    path("update-card/<int:pk>/", update_card, name="update_card"),
]
