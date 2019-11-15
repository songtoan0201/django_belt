from django.db import models
import datetime
from apps.login.models import *


class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['destination']) < 3:
            errors["destination"] = "Destination must be at least 3 characters"
        if len(postData['plan']) < 3:
            errors["plan"] = "Plan must be at least 3 characters"
        if len(postData['destination']) == 0:
            errors["no_destination"] = "Destination must be provided"
        if len(postData['plan']) == 0:
            errors["no_plan"] = "Plan must be provided"
        if len(postData['start_date']) == 0:
            errors["no_start_date"] = "Start date must be provided"
        if len(postData['end_date']) == 0:
            errors["no_end_date"] = "End date must be provided"

        if postData['start_date'] < datetime.datetime.now().strftime('%Y-%m-%d'):
            errors["start_date"] = "Start date should be in the future"

        if postData['end_date'] < postData['start_date']:
            errors["end_date"] = "End date should be after start date"
        return errors


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="create_trips")
    joined_by = models.ManyToManyField(User, related_name="join", null=True)
    objects = TripManager()
