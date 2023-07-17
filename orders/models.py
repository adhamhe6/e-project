from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Order(models.Model):
    STATUS_CHOICES = (
        ('RECIEVED', 'recieved'),
        ('PROCESSED', 'processed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECIEVED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for {self.user.username}"
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart.items.all())

    def unload(self):
        self.cart.items.all().delete()