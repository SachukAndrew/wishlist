from datetime import datetime

from django.shortcuts import render, get_object_or_404


from .models import WishList

from .forms import ProductForm

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {'title': 'Wishlist | about project'})

def list_page(request, pk):
    #view page the wishlist
    #FBV - views основанные на функциях
    #CBV - views основанные на классах

    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        #form.create_at = datetime.now() - delete at future
        instance_product = form.save()
        wishlist.product.add(instance_product)
        wishlist.save()
        print(form.pk, form.title)
    elif request.method == 'GET':
        form = ProductForm()
        #wishlist = get_object_or_404(WishList, pk=pk) - delete at future
    return render(
        request,
        'wish_list.html',
        {
        'wish_list': wishlist,
        'is_owner_list': wishlist.owner == request.user,
        'form': form,
        }
    )

