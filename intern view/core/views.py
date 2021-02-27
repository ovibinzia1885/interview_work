import datetime

from django.http import JsonResponse

from .models import *


# Create your views here.

def cashflow_calculator(request, months):
    titles = list()
    year = datetime.date.today().year
    month = datetime.date.today().month
    # print(month)
    for m in range(months):
        jlogs = JournalLogDetails.objects.filter(
            journal_log__transaction_date__year=year,
            journal_log__transaction_date__month=month,
        )
        cash = 0
        income = 0
        expense = 0
        for j in jlogs:
            if j.account_name.type_of_acc.acc_head.name == 'Assets' and j.account_name.type_of_acc.acc_type_name == 'Cash and Bank':
                cash = cash + j.amount
            elif j.account_name.type_of_acc.acc_head.name == 'Income':
                income = income + j.amount
            elif j.account_name.type_of_acc.acc_head.name == 'Expense':
                expense = expense + j.amount
        cashflow = (cash + income) - expense

        p = {
            'year':   year,
            'month':  month,
            'amount': cashflow,

        }
        titles.append(p)
        print(month)
        print(year)
        if month - 1 < 1:
            month = 12
            year = year - 1
        else:
            month = month - 1
    # titles = [product.title for product in qs]
    return JsonResponse(titles, safe=False)
