from django.urls import path

from cards.views import create, list_all, delete, update, find_by_id, share, share_to_card, list_shared_card_users, remove_share, update_share

app_name = 'cards'

urlpatterns = [
    path("create-card/", create, name="create"),
    path("cards/", list_all, name="list_all"),
    path("cards/<int:pk>/", find_by_id, name="find_by_id"),
    path("delete-card/<int:pk>/", delete, name="delete"),
    path("update-card/<int:pk>/", update, name="update"),
    path("share/", share, name="share"),
    path("share-card/<int:pk>/", share_to_card, name="share"),
    path('list-shared-card/<int:pk>', list_shared_card_users, name='list_shared_card_users'),
    path("remove-share/<int:pk>/", remove_share, name="remove_share"),
    path("update-share/<int:pk>/", update_share, name="update_share"),
]
