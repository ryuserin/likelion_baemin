from django import forms
from .models import Store
from .models import Order

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'