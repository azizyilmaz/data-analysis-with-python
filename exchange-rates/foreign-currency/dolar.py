import pandas
import matplotlib.pyplot as plt

# User 'Tarih' column as index
ds = pandas.read_csv('exchange-rates/data/USD TRY Veri Geçmişi - Investing.com.csv', index_col = 0)

# Hide column
ds = ds.drop('Açılış', axis=1)
ds = ds.drop('Yüksek', axis=1)
ds = ds.drop('Düşük', axis=1)
ds = ds.drop('Fark %', axis=1)

ylabel = 'USD/TRY'

# Change column's name
ds.columns = [ylabel]

# Reverse dataset
ds = ds[::-1]
print(ds)
print(ds.dtypes)

ds.plot(color='blue')

plt.grid()
plt.xlabel('Tarih')
plt.ylabel(ylabel)
plt.title('1 USD kaç TRY?')
plt.legend()
plt.show()
