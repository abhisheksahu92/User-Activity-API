from django.test import TestCase
from django.test import Client
from django.utils import timezone
from django.urls import reverse
from .models import User,ActivityPeriod
import json
from .serializers import UserSerializers,ActivitySerializers

# Create your tests here.
# Setup the data for the testcases.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id='W012A3CDE',real_name="Abhishek Sahu", tz="America/Los_Angeles")
        user = User.objects.get(id='W012A3CDE')
        for x in range(3):
            ActivityPeriod.objects.create(user_id=user, start_time=timezone.now() + timezone.timedelta(days=x),
                                     end_time=timezone.now() + timezone.timedelta(days=x) + timezone.timedelta(minutes=5))

    # Objective: Check user and their activity has been created.
    # Steps: Get the count of user and their activity.
    # Expected Output: Check if the count of user and activity is 1 and 3 respectively.
    def test_user_got_created_count(self):
        query_set_user = User.objects.count()
        query_set_activity = ActivityPeriod.objects.count()
        self.assertEqual(query_set_user,1)
        self.assertEqual(query_set_activity,3)

    # Objective: Check user has been created.
    # Steps: Get all the users from the User model.
    # Expected Output: Check if id,real_name and tz is same as setup data provided.
    def test_user_got_created_data(self):
        query_set_user = User.objects.all()
        for this_user in query_set_user:
            self.assertEqual(this_user.id,'W012A3CDE')
            self.assertEqual(this_user.real_name, 'Abhishek Sahu')
            self.assertEqual(this_user.tz, 'America/Los_Angeles')

    # Objective: Check activity has been created.
    # Steps: Get all the activity from the ActivityPeriod model.
    # Expected Output: Check if user_id is same as setup data provided.
    def test_activity_got_created(self):
        query_set_activity = ActivityPeriod.objects.all()
        for this_activity in query_set_activity:
            self.assertEqual(str(this_activity.user_id),'Abhishek Sahu')

    # Objective: Check api endpoint is active.
    # Steps: Create the request to api endpoint.
    # Expected Output: Check if endpoint is giving status 200.
    def test_useractivity_status_view(self):
        response = self.client.get(reverse('useractivity'))
        self.assertEqual(response.status_code, 200)

    # Objective: Check api endpoint is giving data back.
    # Steps: Get the data by hitting the api endpoint.
    # Expected Output: Check if id and activity_periods have correct value provided in setup.
    def test_useractivity_content_view(self):
        response = self.client.get(reverse('useractivity'))
        self.assertEqual(json.loads(response.content)['members'][0]['id'],'W012A3CDE')
        self.assertEqual(len(json.loads(response.content)['members'][0]['activity_periods']),3)

    # Objective: Check serializer.
    # Steps: Get the user and activity data and provide them as input to serializer.
    # Expected Output: Check if data of user and activity from serializer has 1 and 3 count.
    def test_serializers(self):
        user_for_serial = User.objects.all()
        activity_for_serial = ActivityPeriod.objects.all()

        serializer_user = UserSerializers(user_for_serial,many=True)
        self.assertEqual(len(serializer_user.data),1)

        serializer_activity = ActivitySerializers(activity_for_serial,many=True)
        self.assertEqual(len(serializer_activity.data),3)

