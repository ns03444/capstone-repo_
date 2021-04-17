from django.conf.urls import url
from matplot import views

urlpatterns = [
    url(r'graph_page/', views.candlestick, name='candlestick'),
    # url(r'image_page/', views.myplot, name='myplot'),


]
