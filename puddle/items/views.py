from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

# Create your views here.
def browse(request):
    query= request.GET.get('query', '')
    category = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    if category_id:
        items = items.filter(category__id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'items/browse.html',
                   {'items': items,
                    'query': query,
                    'categories': category,
                    'category_id': int(category_id),
                    })


def detail(request, primary_key):
    item = get_object_or_404(Item, pk=primary_key)
    return render(request, 'items/detail.html', {'item': item})

@login_required
def edit_item(request, primary_key):
    item= get_object_or_404(Item, pk=primary_key, 
                            created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:item_detail',
                            primary_key=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html',
                   {'form': form, 'title': 'Edit Item',
                    })




@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:item_detail',
                            primary_key=item.id)
    else:
        form = NewItemForm()

    return render(request, 'items/form.html',
                   {'form': form, 'title': 'New Item',
                    })

@login_required
def delete(request, primary_key):
    item= get_object_or_404(Item, pk=primary_key, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')