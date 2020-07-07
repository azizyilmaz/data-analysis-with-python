import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')
print(dataset)
turkey = dataset[dataset['Country/Region'] == 'Turkey'][dataset['Confirmed'] > 0]

plt.plot(turkey.ObservationDate, turkey.Confirmed, color='orange', label='Confirmed')
plt.plot(turkey.ObservationDate, turkey.Deaths, color='red', label='Deaths')
plt.xlabel('Observation Date')
plt.ylabel('Count')
plt.title('Turkey Coronavirus Analysis')
plt.legend()

plt.show()
