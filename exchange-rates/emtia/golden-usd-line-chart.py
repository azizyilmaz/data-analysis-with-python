import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv(
    'exchange-rates/data/Altın Vadeli İşlemleri Fiyat Geçmişi - Investing.com.csv')

# Hide column
ds = ds.drop('Açılış', axis=1)
ds = ds.drop('Yüksek', axis=1)
ds = ds.drop('Düşük', axis=1)
ds = ds.drop('Hac.', axis=1)
ds = ds.drop('Fark %', axis=1)

# Change column's name
ds.columns = ['Tarih', 'XAU/USD']

# Reverse dataset's index
ds = ds[::-1].reset_index(drop=True)
print(ds)
print(ds.dtypes)

# Set 'Tarih' to index of dataset
ds.index = pd.to_datetime(ds['Tarih'])
print(ds)
print(ds.dtypes)

ds.plot(color='blue')

plt.grid()
plt.xlabel('Tarih')
plt.ylabel('XAU')
plt.title('SPOT ALTIN/ABD DOLARI')
plt.legend()
plt.show()