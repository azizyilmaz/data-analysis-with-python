import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')

turkey = dataset[dataset['Country/Region'] == 'Turkey']
italy = dataset[dataset['Country/Region'] == 'Italy']

dataset.plot(subplots=True)

plt.subplot(2, 1, 1)
plt.plot(turkey.Deaths, turkey.Recovered, color='red',
         label='Deaths and Recovered in Turkey')
plt.xlabel('Turkey Deaths')
plt.ylabel('Turkey Recovered')

plt.subplot(2, 1, 2)
plt.plot(italy.Deaths, italy.Recovered, color='blue',
         label='Deaths and Recovered in Italy')
plt.xlabel('Italy Deaths')
plt.ylabel('Italy Recovered')

plt.show()
