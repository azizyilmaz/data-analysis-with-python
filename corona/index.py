import pandas

dataset = pandas.read_csv("coronavirusdata/covid_19_data.csv")

print(f'Covid19 veri listesi:\n{dataset}')

print(f'Satır ve sütun sayıları:\n{dataset.shape}')

print(f'Sütunları:\n{dataset.columns}')

print(f'Veri tipleri:\n{dataset.dtypes}')

print(f'İlk 10 veri listesi:\n{dataset.head(10)}')

print(f'Son 10 veri listesi:\n{dataset.tail(10)}')

print(f'Veri listesi bilgileri:\n{dataset.info()}')

print(f'Veri listesi özeti:\n{dataset.describe()}')

# En fazla ölümün olduğu 20 veriyi getirir
print(dataset.sort_values(by="Deaths", ascending=False).head(20))

# Türkiye sonuçları
print(dataset[dataset['Country/Region'] == 'Turkey']
      .sort_values(by="Deaths", ascending=False).head(20))
