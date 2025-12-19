from django.shortcuts import render, redirect
from django.contrib.auth import logout

from items.models import Item, Category
from django.db.models import Count

from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    # annotate categories with the number of items in each (only non-deleted items counted)
    categories = Category.objects.annotate(item_count=Count('item'))
    return render(request, 'core/index.html', 
                  {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:index')