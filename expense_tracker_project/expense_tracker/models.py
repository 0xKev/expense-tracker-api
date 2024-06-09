from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('GROCERIES', 'Groceries'),
        ('LEISURE', 'Leisure'),
        ('ELECTRONICS', 'Electronics'),
        ('UTILITIES', 'Utilities'),
        ('CLOTHING', 'Clothing'),
        ('HEALTH', 'Health'),
        ('OTHERS', 'Others'),
    ]
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    purchase_date = models.DateField("expense date", default=timezone.now().date())
    amount = models.IntegerField("amount spent")
    purchase_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    other_purchase_type = models.CharField(max_length=20, blank=True, null=True)