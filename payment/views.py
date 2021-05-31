import stripe
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import List
from .forms import ListForms
from django.contrib import messages
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    if request.method == 'POST':
        form = ListForms(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,'Item Has Been Added To List!')
            return render(request,'home.html', {'all_items': all_items} )
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})


def payments(request):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Donate for manalap',
            source=request.POST['stripeToken']
        )
        amount = charge.amount / 100
    return render(request, 'payments.html', {})


def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item is deleted!'))
    return redirect('home')


def complete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncomplete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')









'''
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context



        
'''