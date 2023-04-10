from django import forms
from .models import CustomerModel

class CustomerForm(forms.ModelForm):
    class Meta:
         model = CustomerModel
         fields = ["name", "dob","age","gender","phonenumber","email","address","district","branch","accounttype","materialsprovide"]
