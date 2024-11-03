from django.shortcuts import render,redirect
from .models import Concert
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TicketPurchaseForm,PaymentForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def home(request):
    event_obj = get_object_or_404(Concert)
    return render(request,'home.html',{'event': event_obj})

def event_details(request):
    event_obj = get_object_or_404(Concert)
    return render(request, 'event_details.html', {'event1': event_obj})

@login_required
def purchase_ticket(request):
    event_obj = get_object_or_404(Concert)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            purchase_data = form.save(commit=False)
            purchase_data.price = purchase_data.quantity * purchase_data.unit_price
            #purchase_data.save()
            #form.save()
            request.session['purchase_data'] = {
                'purchaser_name': purchase_data.purchaser_name,
                'contact_number': purchase_data.contact_number,
                'payment_method': purchase_data.payment_method,
                'quantity': purchase_data.quantity,
                'price': purchase_data.price  # Include the calculated price
            }
            
            #request.session['purchase_data'] = form.cleaned_data
            return redirect('payment')
    else:
        form = TicketPurchaseForm()
    return render(request, 'purchasing_ticket.html', {'form': form,'event': event_obj})

def payment_view(request):
    purchase_data = request.session.get('purchase_data')
    
    if not purchase_data:
        return redirect('purchaseing_ticket')  # Redirect if no data is found

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the payment here (e.g., using a payment gateway API)
            # For now, let's assume payment is successful
            # Clear the session data after processing payment
            purchase_data.save()
            del request.session['purchase_data']
            return redirect('payment_success')
    else:
        form = PaymentForm()

    total_price = purchase_data.get('price')
    return render(request, 'payment.html', {'form': form, 'purchase_data': purchase_data, 'total_price': total_price})

def payment_success_view(request):
    return render(request, 'payment_success.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # If the form is valid, log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
