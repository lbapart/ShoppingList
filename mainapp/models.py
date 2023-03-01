from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Purchase(models.Model):
    class Types(models.TextChoices):
        QTY = 'QTY', 'qty'
        GR = 'GR', 'gr'
        KG = 'KG', 'kg'
        ML = 'ML', 'ml' 
        L = 'L', 'l'

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=1)
    
    def __str__(self) -> str:
        return f"{self.quantity} {self.title}"
    
    class Meta:
        ordering = ['completed']