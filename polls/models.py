import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
import datetime
from .generator import randomf


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    user = models.OneToOneField(User, null=True)
    dob = models.DateField(default=datetime.date.today)
    age = models.IntegerField(blank=True, null=True)
    rumber = models.IntegerField(default=randomf)
      
    def howold(self):
        today = datetime.date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
 
 
