from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Expense
from .forms import BudgetForm, ExpenseForm
from django.utils import timezone

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

def budget_detail(request, month):
    budget = get_object_or_404(Budget, month=month)
    expenses = Expense.objects.filter(budget=budget)
    total_expense = sum(expense.amount for expense in expenses)
    remaining_budget = budget.amount - total_expense
    return render(request, 'budget_detail.html', {'budget': budget, 'expenses': expenses, 'remaining_budget': remaining_budget})

def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})

def add_expense(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.save()
            return redirect('budget_detail', month=budget.month)
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form, 'budget': budget})

def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('budget_detail', month=expense.budget.month)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('budget_detail', month=expense.budget.month)
    return render(request, 'delete_expense.html', {'expense': expense})
