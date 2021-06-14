from django.db import models


class Customer(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)


class Subscription(models.Model):
    customer = models.OneToOneField(Customer, related_name='subscription', on_delete=models.CASCADE)
    id = models.CharField(max_length=60, primary_key=True)
    plan_name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)


class Gift(models.Model):
    customer = models.ForeignKey(Customer, related_name='gifts', on_delete=models.CASCADE)
    id = models.CharField(max_length=60, primary_key=True)
    plan_name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    recipient_email = models.CharField(max_length=30)


class Record(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
