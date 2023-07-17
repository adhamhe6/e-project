from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from cart.models import Cart

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('view_cart')
    order = Order.objects.create(cart=cart, user=request.user)
    order.unload()
    cart.status = 'COMPLETED'
    cart.save()
    messages.success(request, "Your order has been placed.")
    return redirect('view_invoice', order_id=order.id)

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/view_orders.html', {'orders': orders})

@login_required
def view_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/view_invoice.html', {'order': order})