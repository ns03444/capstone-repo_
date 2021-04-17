from django.shortcuts import render
from stock_app.models import Stock

def stock_page(request):
    stock_lst = Stock.objects.all()[:25]
    context = {
        'stock_objects': stock_lst,
    }
    return render(request, 'stock_page.html', context)
