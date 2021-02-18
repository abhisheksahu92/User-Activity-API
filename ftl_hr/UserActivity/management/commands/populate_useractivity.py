#third-party packages
from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from datetime import timedelta
import random,string
import pytz

# Project packages
from UserActivity.models import User,ActivityPeriod

# Creating basecommand to populate date with default 10 users and their 5 activity.
class Command(BaseCommand):
    help = 'Seed the User Activity database'

    def add_arguments(self, parser):
        parser.add_argument('--user',
                            default=10,
                            type=int,
                            help='The number of User you want to create.')
        parser.add_argument('--activity',
                            default=5,
                            type=int,
                            help='The number of activity you want to create.')

    def handle(self,*args,**kwargs):
        fake = Faker()
        try:
            # Creating users.
            for _ in range(kwargs['user']):
                _user_id = 'W' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                User.objects.create(id=_user_id,real_name=fake.name(),tz=random.choice(pytz.all_timezones))

            # Creating activities of each users.
            for user in User.objects.all():
                for activity in range(kwargs['activity']):
                    this_start_date = fake.date_time_between(start_date='-1y', end_date='now')
                    this_end_date = this_start_date + timedelta(minutes=5)
                    start_time = timezone.make_aware(this_start_date, timezone.get_current_timezone())
                    end_time  = timezone.make_aware(this_end_date, timezone.get_current_timezone())
                    ActivityPeriod.objects.create(user_id=user,start_time=start_time,end_time=end_time)

        except Exception as e:
            print(f'Creation Errors: {e}')