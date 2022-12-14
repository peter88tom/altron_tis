from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.forms import CustomerInformationForm
from app.models import CustomerFinancialInformation, CustomerInformation
from django.views.decorators.csrf import csrf_exempt
import openpyxl

# Create your views here.
def index(request):
  return render(request, 'index.html')


# Create new user information
def post_new_user_information(request):
  if request.method == 'POST':
    new_user_information = CustomerInformationForm(request.POST, request.FILES)
    if new_user_information.is_valid():
      print("Form is valid")
      new_user_information.save()

      # Extract data from excel file and save it to the database
      excel_file = request.FILES['uploaded_file']

      wb = openpyxl.load_workbook(excel_file, data_only=True)

      # Get a sheet name
      worksheet = wb["Sheet1"]

      excel_data  = list()

      # Iterating over the rows and getting values from each cell in row
      for row in worksheet.iter_rows(min_row=2):
        row_data = list()
        for cell in row:
          row_data.append(str(cell.value))
        excel_data.append(row_data)

      # Save financial information to the database
      for row in excel_data:
        new_financial_information = CustomerFinancialInformation()
        new_financial_information.customer = CustomerInformation.objects.get(pk=new_user_information.instance.id)
        new_financial_information.month = row[0]
        new_financial_information.income = row[1]
        new_financial_information.expenses = row[2]

        new_financial_information.save()

    else:
      print("Form is not valid")
      return redirect('/')
  return redirect('/')



@csrf_exempt
def get_latest_income_and_expenses(request):
  data = []
  data_months = CustomerFinancialInformation.objects.all().order_by('-id')[:12][::-1]
  for m in data_months:
    k = {
      'month':m.month,
      'income':m.income,
      'expense': m.expenses,
    }
    data.append(k)
  try:
    return JsonResponse(data, safe=False)
  except Exception as e:
    return JsonResponse(data, safe=False)
