from django.shortcuts import render, redirect
from .models import Subscription
from django import forms
from django.contrib.auth.decorators import login_required

# Form
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'price', 'billing_cycle', 'next_renewal']

# Views
@login_required
def subscription_list(request):
    subs = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/list.html', {'subs': subs})

@login_required
def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.user = request.user
            sub.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscriptions/add.html', {'form': form})
