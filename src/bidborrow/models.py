from django.db import models

# Create your models here.
class Application(models.Model):
    borrower = models.CharField(default="John Smith", max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=40, default=10000)

class Bid(models.Model):
    lender = models.CharField(default="The Bank", max_length=100)
    borrower = models.CharField(default="John Smith", max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=40, default=10000)
    discount = models.DecimalField(decimal_places=2,
                                   max_digits=4,
                                   default=0.1)
    repayment = models.DecimalField(decimal_places=2,
                                    max_digits=4,
                                    default=0.1)
