from django.shortcuts import render
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','capstone_project.settings')
import django
django.setup()
import requests
from pandas_datareader import data as web
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import HoverTool

def candlestick(request):
    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2021,4,2)
    df= web.DataReader(name='^GSPC', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value
    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    p=figure(x_axis_type='datetime', width=1000, height=500)
    p.title='S&P 500: Year to Date'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    p.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    p.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    p.segment(df.index, df.High, df.index, df.Low, color='black')

    script, div = components(p)

    start = datetime.datetime(2020,3,28)
    end = datetime.datetime(2021,4,2)
    df= web.DataReader(name='^GSPC', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value

    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    plot=figure(x_axis_type='datetime', width=1000, height=500)
    plot.title='S&P 500: Post Covid Pandemic'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    plot.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    plot.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    plot.segment(df.index, df.High, df.index, df.Low, color='black')
    scripts, divs = components(plot)
    start = datetime.datetime(2016,4,2)
    end = datetime.datetime(2021,4,2)
    df= web.DataReader(name='^GSPC', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value

    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    plots=figure(x_axis_type='datetime', width=1000, height=500)
    plots.title='S&P 500: 2016-present'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    plots.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    plots.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    plots.segment(df.index, df.High, df.index, df.Low, color='black')
    script1, div1 = components(plots)

    return render(request, 'graph_page.html', {'script':script, 'div':div, 'scripts': scripts, 'divs': divs,'script1':script1, 'div1':div1})




# def myplot(request):
#     return render(request, 'image_page.html')
# start = datetime.datetime(2016,5,2)
# end = datetime.datetime(2021,5,2)
# vz = web.DataReader(name='VZ', data_source = 'yahoo', start=start, end=end)
# att = web.DataReader(name='T', data_source = 'yahoo', start=start, end=end)
# tmus = web.DataReader(name='TMUS', data_source = 'yahoo', start=start, end=end)
# vz.to_csv(r'VZ.csv')
# att.to_csv(r'T.csv')
# tmus.to_csv(r'TMUS.csv')
# def closing_prices(request):
#
#     vz['Close'].plot(label='Verizon', figsize=(8,8))
#     att['Close'].plot(label='AT&T')
#     tmus['Close'].plot(label='T-Mobile')
#     plt.title('Closing Prices')
#     fig=plt.gcf()
#     buf=io.BytesIO()
#     fig.savefig(buf, format='png')
#     buf.seek(0)
#     string= base64.b64encode(buf.read())
#     uri = urllib.parse.quote(string)
#     return render(request, 'more.html', {'close':uri})


    # vz['Volume'].plot(label='Verizon Volume')
    # att['Volume'].plot(label='AT&T Volume')
    # tmus['Volume'].plot(label='T-Mobile Volume')
    # plt.title('Volume')
    # fig1=plt.gcf()
    # buf1=io.BytesIO()
    # fig1.savefig(buf1, format='png')
    # buf1.seek(0)
    # string1= base64.b64encode(buf1.read())
    # uri1 = urllib.parse.quote(string1)


    #using daily returns to compare stock volatility --- most volatile == T-Mobile (highest st. dev.)
    # vz['Returns']= (vz['Close']/vz['Open'].shift(1)) - 1
    # att['Returns']= (att['Close']/att['Open'].shift(1)) - 1
    # tmus['Returns']= (tmus['Close']/tmus['Open'].shift(1)) - 1
    # vz['Returns'].hist(bins=100, label='VZ', alpha=0.5)
    # att['Returns'].hist(bins=100, label='T', alpha=0.5)
    # tmus['Returns'].hist(bins=100, label='TMUS', alpha=0.5)
    # plt.title('Volatility')
    # fig2=plt.gcf()
    # buf2=io.BytesIO()
    # fig2.savefig(buf2, format='png')
    # buf2.seek(0)
    # string2= base64.b64encode(buf2.read())
    # uri2 = urllib.parse.quote(string2)

    # vz['Market Cap'] = vz['Close']* vz['Volume']
    # att['Market Cap'] = att['Close']* att['Volume']
    # tmus['Market Cap'] = tmus['Close']* tmus['Volume']
    # vz['Market Cap'].hist(bins=100, label='VZ', alpha=0.5)
    # att['Market Cap'].hist(bins=100, label='T', alpha=0.5)
    # tmus['Market Cap'].hist(bins=100, label='TMUS', alpha=0.5)
    # plt.title('Market Cap')
    # fig3=plt.gcf()
    # buf3=io.BytesIO()
    # fig3.savefig(buf3, format='png')
    # buf3.seek(0)
    # string3= base64.b64encode(buf3.read())
    # uri3 = urllib.parse.quote(string3)
    # return render(request, 'more.html', {'close':uri,'volume':uri1, 'volatility': uri2})
#     vz['Volume'].plot(label='Verizon Volume')
#     att['Volume'].plot(label='AT&T Volume')
#     tmus['Volume'].plot(label='T-Mobile Volume')
#     plt.title('Volume')
#     plt.legend()
#     fig=plt.gcf()
#     buf=io.BytesIO()
#     fig.savefig(buf, format='png')
#     buf.seek(0)
#     string= base64.b64encode(buf.read())
#     uri1 = urllib.parse.quote(string)
#     return render(request, 'more.html', {'data1':uri1})
# def graph_page(request):
    # df = pd.read_csv('matplot\export_TMUS.csv')
    # df=df[['Close']]
    # future_days=5
    # df['Predicted Prices'] = df[['Close']].shift(-future_days)
    # x = np.array(df.drop(['Predicted Prices'], 1))[:-future_days]
    # y = np.array(df['Predicted Prices'])[:-future_days]
    # #splitting data into 75% training-set & 25% test-set
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # #creating decision tree model
    # tree = DecisionTreeRegressor().fit(x_train, y_train)
    # lr = LinearRegression().fit(x_train, y_train)
    # x_future = df.drop(['Predicted Prices'], 1)[:-future_days]
    # x_future = x_future.tail(future_days)
    # x_future = np.array(x_future)
    # tree_pred = tree.predict(x_future)
    # lr_pred = lr.predict(x_future)
    # preds = tree_pred
    # valid = df[x.shape[0]:]
    # valid['Predicted Prices']= preds
    # #tree predicted price= $126.30 -- lr pp= 124.67
    # plt.figure(figsize=(16,10))
    # plt.title('T-mobile: Decision Tree Model')
    # plt.xlabel('Days')
    # plt.ylabel('Close Price')
    # plt.plot(df['Close'])
    # plt.plot(valid[['Close', 'Predicted Prices']])
    # plt.show()
    # start = datetime.datetime(2021,1,1)
    # end = datetime.datetime(2021,4,2)
    # df= data.DataReader(name='VZ', data_source = 'yahoo', start=start, end=end)
    # def inc_dec(c, o):
    #     if c > o:
    #         value= 'increase'
    #     elif c < o:
    #         value='decrease'
    #     else:
    #         value="Equal"
    #     return value
    #
    # df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    # df['Middle']=(df.Open+df.Close)/2
    # df['Height']=abs(df.Open - df.Close)
    #
    #
    # p=figure(x_axis_type='datetime', width=1000, height=500)
    # p.title='verizon candlestick chart'
    # # p.grid.grid_line_alpha=0.3
    # hours= 12*60*60*1000
    # p.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
    #         hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')
    #
    # p.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
    #         hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    # p.segment(df.index, df.High, df.index, df.Low, color='black')
    # output_file('candlestick.html')
    # show(p)
    #
    # # fig = p.gcf()
    # # buf = io.BytesIO()
    # # fig.savefig(buf, format='png')
    # # buf.seek(0)
    # # string = base64.b64encode(buf.read())
    # # uri = urllib.parse.quote(string)
    # return render(request, 'graph_page.html')


# Create your views here.
