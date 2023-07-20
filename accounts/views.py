from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import UserProfile

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks
            return redirect(reverse('accounts:register'))
        else:
            error_message = "The email address or password you entered is incorrect."
    else:
        error_message = None
    return render(request, 'registration/login.html', {'error_message': error_message})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # full_name = form.cleaned_data['full_name']
            # email = form.cleaned_data['email']
            # profile = UserProfile.objects.create(user=user, full_name=full_name, email=email)
            regular_users_group, created = Group.objects.get_or_create(name='Regular Users')
            regular_users_group.user_set.add(user)
            login(request, user)
            return redirect('home')
        else:
            error_message = "Please correct the errors below."
    else:
        form = CustomUserCreationForm()
        error_message = None
    return render(request, 'accounts/register.html', {'form': form, 'error_message': error_message})

@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        if full_name:
            user.first_name, user.last_name = full_name.split(maxsplit=1)
        if email:
            user.email = email
        user.save()
        data = {'success': True, 'message': 'Profile updated successfully.'}
    else:
        data = {'success': False, 'message': 'Invalid request method.'}
    return JsonResponse(data)



""" from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages """


'''
{% if error_message %}
    <p>{{ error_message }}</p>
{% endif %}
'''

'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
'''
""" 
@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payment_list.html', {'payments': payments})

@login_required
def payment_add(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        payment = Payment(user=request.user, card_number=card_number)
        payment.save()
        messages.success(request, 'Payment information added successfully.')
        return redirect('payment_list')
    return render(request, 'payment_form.html', {'title': 'Add Payment Information'})

@login_required
def payment_edit(request, pk):
    payment = get_object_or_404(Payment, pk=pk, user=request.user)
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        payment.card_number = card_number
        payment.save()
        messages.success(request, 'Payment information updated successfully.')
        return redirect('payment_list')
    return render(request, 'payment_form.html', {'payment': payment, 'title': 'Edit Payment Information'})

@login_required
def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk, user=request.user)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment information deleted successfully.')
        return redirect('payment_list')
    return render(request, 'payment_confirm_delete.html', {'payment': payment})

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_list.html', {'contacts': contacts})

@login_required
def contact_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        number = request.POST.get('number')
        contact = Contact(user=request.user, title=title, number=number)
        contact.save()
        messages.success(request, 'Contact added successfully.')
        return redirect('contact_list')
    return render(request, 'contact_form.html', {'title': 'Add Contact'})

@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        number = request.POST.get('number')
        contact.title = title
        contact.number = number
        contact.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('contact_list')
    return render(request, 'contact_form.html', {'contact': contact, 'title': 'Edit Contact'})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})

@login_required
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'address_list.html', {'addresses': addresses})

@login_required
def address_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        address = request.POST.get('address')
        address = Address(user=request.user, title=title, address=address)
        address.save()
        messages.success(request, 'Address added successfully.')
        return redirect('address_list')
    return render(request, 'address_form.html', {'title': 'Add Address'})

@login_required
def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        address_text = request.POST.get('address')
        address.title = title
        address.address = address_text
        address.save()
        messages.success(request, 'Address updated successfully.')
        return redirect('address_list')
    return render(request, 'address_form.html', {'address': address, 'title': 'Edit Address'})

@login_required
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'Address deleted successfully.')
        return redirect('address_list')
    return render(request, 'address_confirm_delete.html', {'address': address}) """

""" from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm, ContactNumberForm, DeliveryAddressForm, PaymentOptionForm
from .models import User, ContactNumber, DeliveryAddress, PaymentOption

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    contact_numbers = user.contact_numbers.all()
    delivery_addresses = user.delivery_addresses.all()
    payment_options = user.payment_options.all()
    return render(request, 'profile.html', {
        'user': user,
        'contact_numbers': contact_numbers,
        'delivery_addresses': delivery_addresses,
        'payment_options': payment_options,
    })


@login_required
def add_contact_number(request):
    if request.method == 'POST':
        form = ContactNumberForm(request.POST)
        if form.is_valid():
            contact_number = form.save(commit=False)
            contact_number.user = request.user
            contact_number.save()
            return redirect('profile')
    else:
        form = ContactNumberForm()
    return render(request, 'add_contact_number.html', {'form': form})


@login_required
def add_delivery_address(request):
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():
            delivery_address = form.save(commit=False)
            delivery_address.user = request.user
            delivery_address.save()
            return redirect('profile')
    else:
        form = DeliveryAddressForm()
    return render(request, 'add_delivery_address.html', {'form': form})


@login_required
def add_payment_option(request):
    if request.method == 'POST':
        form = PaymentOptionForm(request.POST)
        if form.is_valid():
            payment_option = form.save(commit=False)
            payment_option.user = request.user
            payment_option.save()
            return redirect('profile')
    else:
        form = PaymentOptionForm()
    return render(request, 'add_payment_option.html', {'form': form}) """