import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

plt.style.use('ggplot')

# To read or import data from CSV file
data = pd.read_csv('exchange-rates/data/USD TRY Veri Geçmişi - Investing.com.csv')
# Select columns by name
ohlc = data.loc[:, ['Tarih', 'Açılış', 'Yüksek', 'Düşük', 'Şimdi']]
ohlc['Tarih'] = pd.to_datetime(ohlc['Tarih'])
ohlc['Tarih'] = ohlc['Tarih'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

fig, ax = plt.subplots()

candlestick_ohlc(ax,
                 ohlc.values,
                 width=0.6,
                 colorup='green',
                 colordown='red',
                 alpha=0.8)

ax.set_xlabel('Tarih')
ax.set_ylabel('TRY')
fig.suptitle('Daily Candlestick Chart of USD/TRY (2010~2020)')

date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()
fig.tight_layout()

plt.show()