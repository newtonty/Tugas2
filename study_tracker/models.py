from django.db import models

class AssignmentRecord(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()
