import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')

turkey = dataset[dataset['Country/Region'] == 'Turkey'].groupby(
    ['ObservationDate']).agg(
        sum_Confirmed=('Confirmed', 'sum'),
        sum_Deaths=('Deaths', 'sum'),
    ).reset_index()
italy = dataset[dataset['Country/Region'] == 'Italy'].groupby(
    ['ObservationDate']).agg(
        sum_Confirmed=('Confirmed', 'sum'),
        sum_Deaths=('Deaths', 'sum'),
    ).reset_index()

dataset.plot(subplots=True)

plt.subplot(2, 1, 1)
plt.plot(turkey.sum_Confirmed,
         turkey.sum_Deaths,
         color='red',
         label='Deaths and Confirmed in Turkey')
plt.xlabel('Turkey Confirmed')
plt.ylabel('Turkey Deaths')

plt.subplot(2, 1, 2)
plt.plot(italy.sum_Confirmed,
         italy.sum_Deaths,
         color='blue',
         label='Deaths and Confirmed in Italy')
plt.xlabel('Italy Confirmed')
plt.ylabel('Italy Deaths')

plt.show()
