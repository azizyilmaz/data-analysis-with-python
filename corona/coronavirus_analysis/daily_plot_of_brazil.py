import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')
brazil = dataset[dataset['Country/Region'] == 'Brazil'][
    dataset['Confirmed'] > 0].groupby(['ObservationDate']).agg(
        sum_Confirmed=('Confirmed', 'sum'),
        sum_Deaths=('Deaths', 'sum'),
    ).reset_index()
print(brazil)

# Set index as datetime
brazil.index = pandas.to_datetime(brazil['ObservationDate'])
print(brazil)
print(brazil.dtypes)

plt.grid()
plt.plot(brazil.index, brazil.sum_Confirmed, color='orange', label='Confirmed')
plt.plot(brazil.index, brazil.sum_Deaths, color='red', label='Deaths')
plt.xlabel('Observation Date')
plt.ylabel('Count')
plt.title('Brazil Coronavirus Analysis')
plt.legend()
plt.show()
