import os
import sys
import django
from pathlib import Path


DJANGO_BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'potentialpancake.settings'
django.setup()

if __name__ == '__main__':
    from django.contrib.auth.models import Group, Permission

    group_permissions = {
        'admin': ['view_card', 'add_task', 'change_task', 'delete_task', 'view_task'],
        'user': ['view_card', 'view_task'],
    }

    for group_name, permissions in group_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        group.permissions.set(Permission.objects.filter(codename__in=permissions))
