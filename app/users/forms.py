from django import forms

class EmployeeSearchForm(forms.Form):
    employee_code = forms.IntegerField(label='Employee Code', required=True)