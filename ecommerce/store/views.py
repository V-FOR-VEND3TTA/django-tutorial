from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'yourappname/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Initialize the cart in the session if not already present
    if 'cart' not in request.session:
        request.session['cart'] = {}

    # Add the product to the cart or increment its quantity
    if product_id in request.session['cart']:
        request.session['cart'][product_id]['quantity'] += 1
    else:
        request.session['cart'][product_id] = {'quantity': 1}

    return HttpResponseRedirect(reverse('product_list'))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            return redirect('product_list')  # Redirect to the product list or any desired page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'store/login.html', {'form': form})

