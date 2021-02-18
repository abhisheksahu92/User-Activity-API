from django.db import models
from django.core.validators import RegexValidator

# User Model
class User(models.Model):
    id = models.CharField(primary_key=True,max_length=7,validators=[RegexValidator(regex='^.{7}$', message='Length has to be 7', code='nomatch')])
    real_name = models.CharField(null=False,blank=False,max_length=30)
    tz = models.CharField(null=False,blank=False,max_length=30)

    def __str__(self):
        return self.real_name

# Activity Period Model
class ActivityPeriod(models.Model):
    user_id = models.ForeignKey(User,related_name='activity_periods',on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=False,blank=False)
    end_time   = models.DateTimeField(null=False,blank=False)

    class Meta:
        ordering = ['start_time']
