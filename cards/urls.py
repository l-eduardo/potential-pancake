from django.urls import path

from cards.views import create, list_all, delete, update, find_by_id, share, share_to_card

app_name = 'cards'

urlpatterns = [
    path("create-card/", create, name="create"),
    path("cards/", list_all, name="list_all"),
    path("cards/<int:pk>/", find_by_id, name="find_by_id"),
    path("delete-card/<int:pk>/", delete, name="delete"),
    path("update-card/<int:pk>/", update, name="update"),
    path("share/", share, name="share"),
    path("share-card/<int:pk>/", share_to_card, name="share")
]
