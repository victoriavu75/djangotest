from django.db import models

class volunteers(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    vol_id = models.IntegerField()

    def __str__(self):
        return self.firstname
