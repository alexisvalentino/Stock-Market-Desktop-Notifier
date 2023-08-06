import datetime
import time
from plyer import notification
from alpha_vantage.timeseries import TimeSeries

api_key = '<insert api key>'
ts = TimeSeries(key=api_key)

while True:
    data, metadata = ts.get_quote_endpoint(symbol='TSLA')

    notification.notify(
        title="TSLA data ({})".format(datetime.date.today()),
        message="Current Price = {}, \nDayLow = {}, \nDayHigh ={}".format(
            data['05. price'],
            data['04. low'],
            data['03. high']
        ),
        app_icon="C:/Users/Desktop/image.ico",
        timeout=5
    )

    time.sleep(60*60*2)