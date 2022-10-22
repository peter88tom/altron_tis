from django import forms
from app.models import CustomerFinancialInformation, CustomerInformation


class CustomerInformationForm(forms.ModelForm):
  first_name = forms.CharField(max_length=200, required=True)
  last_name = forms.CharField(max_length=200, required=True)
  date_of_birth = forms.CharField(max_length=200, required=True)
  uploaded_file = forms.FileField(required=True)

  class Meta:
    model = CustomerInformation
    fields = ('first_name', 'last_name', 'date_of_birth', 'uploaded_file')
