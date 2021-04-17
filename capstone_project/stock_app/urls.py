from django.conf.urls import url
from stock_app import views

urlpatterns = [
    url(r'stock_page/', views.stock_page, name='stock_page'),


]
