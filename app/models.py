from django.db import models

# Model to store customer information
class CustomerInformation(models.Model):
  first_name = models.CharField(max_length=250, blank=False)
  last_name = models.CharField(max_length=250, blank=False)
  date_of_birth = models.DateField(blank=False)
  uploaded_file = models.FileField(null=True, blank=True, upload_to='uploaded_excel_files/')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


# Schema to store customer financial information once they upload the excel file
class CustomerFinancialInformation(models.Model):
  customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE, null=True, blank=True)
  month = models.CharField(max_length=100, blank=False)
  income = models.DecimalField(max_digits=10, decimal_places=2)
  expenses = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.customer.first_name} {self.customer.last_name} - {self.month}"

