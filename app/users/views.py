from django.shortcuts import render
from .models import User, Bonus
from .forms import EmployeeSearchForm

def index(request):
    return render(request,"index.html",)

def search_employee(request):
    form = EmployeeSearchForm(request.POST or None)
    employee = None
    error_message = None
    calculated_rate = None
    bonuses = None

    if request.method == 'POST':
        if form.is_valid():
            employee_code = form.cleaned_data['employee_code']
            try:
                employee = User.objects.get(employee_code=employee_code)
                calculated_rate = employee.rate * 225 if employee.rate else None
                bonuses = Bonus.objects.filter(payout__user=employee)
            except User.DoesNotExist:
                error_message = 'Employee with the given code does not exist.'

    context = {
        'form': form,
        'employee': employee,
        'calculated_rate': calculated_rate,
        'bonuses': bonuses,
        'error_message': error_message
    }
    return render(request, 'search_employee.html', context)
