from django.shortcuts import render, get_object_or_404, redirect
from .models import Store
from .forms import StoreForm
from .forms import OrderForm

# Create your views here.

def home(request):
    stores = Store.objects.all()
    store_cnt = Store.objects.count()
	    
    return render(request, 'baeminapp/home.html', {"stores": stores, "store_cnt": store_cnt})

def detail(request, store_id):
    store = get_object_or_404(Store, id = store_id)

    return render(request, 'baeminapp/detail.html', {'store': store})

def create(request):
    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save()
            return redirect('detail', store.id)
    else:
        form = StoreForm()
        return render(request, 'baeminapp/create.html', {"form": form})

def order(request, store_id):
    store = get_object_or_404(Store, id = store_id)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            return render(request, 'baeminapp/order_success.html')  
    else:
        form = OrderForm()
        return render(request, 'baeminapp/order.html', {"form": form})   

def order_success(request):
    return render(request, 'baeminapp/order_success.html')     