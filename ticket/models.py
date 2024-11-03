from django.db import models
from django.core.validators import RegexValidator
import random
from django.contrib.auth.models import User


class Concert(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='concert_images/', blank=True, null=True)
    max_ticket = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title
    
class Ticket(models.Model):
        PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        # Add more payment methods as needed
      ]
        payment_method = models.CharField(
            max_length=20,
            choices=PAYMENT_METHOD_CHOICES,
            default='credit_card',
            )
        ticket_id = models.CharField(max_length=6, unique=True, blank=True)
        contact_number = models.CharField(max_length=15, null=True, blank=True)
        purchaser_name = models.CharField(max_length=100,null=True, blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
        quantity = models.PositiveIntegerField(default=0)
        unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)  # Example unit price
        card_number = models.CharField(
                        max_length=19,
                        validators=[
                            RegexValidator(
                                regex=r'^\d{13,19}$',
                                message='Card number must be between 13 and 19 digits.',
                            )
                        ],
                        help_text="Enter the card number without spaces or dashes.",
                        default='0000000000000000',
                    )
        def save(self, *args, **kwargs):
          self.price = self.quantity * self.unit_price
          if not self.ticket_id:
            self.ticket_id = str(random.randint(100000, 999999))
          super(Ticket, self).save(*args, **kwargs) 

class Payment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
