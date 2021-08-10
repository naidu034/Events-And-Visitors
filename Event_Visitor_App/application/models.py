from django.db import models
from django.utils.timezone import now

# Create your models here.


class Visitor(models.Model):
    datetime = models.DateTimeField(default=now, editable=False)
    visitorname = models.CharField(max_length=50)
    tomeet = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    address = models.TextField()
    purpose = models.TextField()
    mobile = models.IntegerField(max_length=10)

    class Meta:
        db_table = "Visitor"

    def __str__(self):
        return self.visitorname


