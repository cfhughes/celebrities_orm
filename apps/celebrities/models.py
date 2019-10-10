from django.db import models

class Celebrity(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    age = models.IntegerField()
    industry = models.CharField(max_length=30)
    income = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
