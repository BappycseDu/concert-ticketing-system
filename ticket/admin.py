from django.contrib import admin
from .models import Concert
from .models import Ticket

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date', 'venue', 'price','image','time','max_ticket')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_id','purchaser_name','contact_number', 'payment_method', 'quantity','price']
