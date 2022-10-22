from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from app.forms import CustomerInformationForm

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = CustomerInformationForm(request.POST, request.FILES)
    if form.is_valid():
      print("Form is valid")
      form.save()
    else:
      print("Form is not valid")
      messages.warning(request, 'Form is not valid')
      return redirect('/')

  return render(request, 'index.html')
