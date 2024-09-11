from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_list, name='budget_list'),
    path('budget/<str:month>/', views.budget_detail, name='budget_detail'),
    path('add_budget/', views.add_budget, name='add_budget'),
    path('add_expense/<int:budget_id>/', views.add_expense, name='add_expense'),
    path('edit_expense/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
]
