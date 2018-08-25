from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'cost/expenses.html', context)



def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form': form})


def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'cost/edit_expense.html', { 'form' : form})


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('cost-list')
