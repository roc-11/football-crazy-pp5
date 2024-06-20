from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponseRedirect
)

from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display the user's order history.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """
    Display the user's wishlist.
    This view renders the user's wishlist page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = Product.objects.filter(users_wishlist=request.user)

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': products,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, id, *args, **kwargs):
    """
    This view handles adding to, and removing a products from,
    the user's wishlist.
    Renders the user's wishlist page.
    """
    product_wish = get_object_or_404(Product, pk=id)
    user = request.user
    user_profile = user.userprofile

    liked = False

    if product_wish.users_wishlist.filter(id=request.user.id).exists():
        product_wish.users_wishlist.remove(request.user)
        messages.success(
            request,
            f'Successfully removed {product_wish} from Wishlist!'
        )
        liked = False
    else:
        product_wish.users_wishlist.add(request.user)
        messages.success(
            request, f'Successfully added {product_wish} to Wishlist!'
        )
        liked = True

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
