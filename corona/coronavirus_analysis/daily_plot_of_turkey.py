import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')
turkey = dataset[dataset['Country/Region'] == 'Turkey'][dataset['Confirmed'] > 0]
print(turkey)

# Set index as datetime
turkey.index = pandas.to_datetime(turkey['ObservationDate'])
print(turkey)
print(turkey.dtypes)

plt.grid()
plt.plot(turkey.index, turkey.Confirmed, color='orange', label='Confirmed')
plt.plot(turkey.index, turkey.Deaths, color='red', label='Deaths')
plt.xlabel('Observation Date')
plt.ylabel('Count')
plt.title('Turkey Coronavirus Analysis')
plt.legend()
plt.show()
