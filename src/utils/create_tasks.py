import os
import sys
import django
from pathlib import Path
from random import choice

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'potentialpancake.settings'

django.setup()

if __name__ == '__main__':
    import faker
    from tasks.models import Card, Task
    from django.contrib.auth.models import User

    Card.objects.all().delete()
    Task.objects.all().delete()

    fake = faker.Faker('pt_BR')

    owner = User.objects.create_user(username='user',
                                    email='user@email.com',
                                    password='password')

    cards = ['Trabalho', 'Faculdade', 'Casa']
    cards_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris non condimentum lectus. '\
                             'Vivamus id commodo turpis. Duis commodo a urna non posuere.'

    django_cards = [Card(title=title, description=cards_description, owner=owner) for title in cards]

    for card in django_cards:
        card.save()

    django_tasks = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        title = fake.text(max_nb_chars=100)
        description = fake.text(max_nb_chars=255)
        card = choice(django_cards)

        django_tasks.append(Task(title=title, description=description, card=card))

    if len(django_tasks) > 0:
        Task.objects.bulk_create(django_tasks)
