import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')

# Grafikteki SNo sütununu siliyor
# axis : {0 or 'index', 1 or 'columns'}
dataset = dataset.drop('SNo', axis=1)

# Türkiye verilerini seçiyor
turkey = dataset[dataset['Country/Region'] == 'Turkey']

# x eksenine ölümler, y eksenine kurtulanlar atanıyor
# Grafik çizgisi kırmızıya boyanıyor ve başlıklar yazılıyor
plt.plot(turkey.Deaths, turkey.Recovered, color='red',
         label='Deaths and Recovered in Turkey')
plt.xlabel('Deaths')
plt.ylabel('Recovered')
plt.title('Turkey Coronavirus Analysis')
plt.legend()

plt.show()
