from django import forms
from django.forms import ModelForm
from .models import MenuItem, Booking

# ClassForm: MenuForm
class MenuItemForm(forms.Form):
    item_name = forms.CharField(max_length = 200)
    category = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000)


# ModelForm: BookingForm
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"