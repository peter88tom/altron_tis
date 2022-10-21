from django.contrib import admin
from app.models import CustomerInformation, CustomerFinancialInformation

# Register your models here.
admin.site.register(CustomerInformation)
admin.site.register(CustomerFinancialInformation)
