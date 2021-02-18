from django.core.management.base import BaseCommand
from django.db import transaction
from UserActivity.models import User,ActivityPeriod

class Command(BaseCommand):
    help = 'Delete the User Activity database'

    @transaction.atomic
    def handle(self,*args,**kwargs):
        User.objects.all().delete()
        ActivityPeriod.objects.all().delete()