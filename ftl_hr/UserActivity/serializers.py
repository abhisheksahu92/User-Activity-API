from rest_framework import serializers
from .models import User,ActivityPeriod

# Serializer for ActivityPeriod
class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

    # Change the representation of start_time and end_time
    def to_representation(self, instance):
        representation = super(ActivitySerializers, self).to_representation(instance)
        representation['start_time'] = instance.start_time.strftime('%b %d %Y %I:%M %p')
        representation['end_time'] = instance.end_time.strftime('%b %d %Y %I:%M %p')
        return representation


# Serializer for User
class UserSerializers(serializers.HyperlinkedModelSerializer):
    activity_periods = ActivitySerializers(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']