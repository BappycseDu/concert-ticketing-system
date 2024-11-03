from django import forms
from django.core.validators import RegexValidator
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['purchaser_name','contact_number','quantity']
        

    #contact_number = forms.CharField(max_length=15, null=True, blank=True)

    
    def __init__(self, *args, **kwargs):
        super(TicketPurchaseForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['price'].initial = self.instance.quantity * self.instance.unit_price
     
    quantity = forms.IntegerField()

class PaymentForm(forms.Form):   
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))      
    payment_method = forms.ChoiceField(choices=Ticket.PAYMENT_METHOD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']