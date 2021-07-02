from django.db import models
from django.conf import settings

# settings.configure()

class Applications(models.Model):
    name = models.CharField(max_length=50)
    description	= models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    framework = models.CharField(max_length=30)
    domain_name	= models.CharField(max_length=50)
    screenshot= models.CharField(max_length=30)
    subscription= models.ForeignKey('subscriptions', on_delete=models.CASCADE)
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Plans(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Subscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE,)
    app = models.ForeignKey(Applications, on_delete=models.CASCADE,)
    active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()