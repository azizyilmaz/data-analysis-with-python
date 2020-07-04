import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('coronavirusdata/covid_19_data.csv')

turkey = dataset[dataset['Country/Region'] == 'Turkey']
italy = dataset[dataset['Country/Region'] == 'Italy']
spain = dataset[dataset['Country/Region'] == 'Spain']

plt.scatter(turkey.Deaths, turkey.Recovered, color='red', label='Turkey')
plt.scatter(italy.Deaths, italy.Recovered, color='blue', label='Italy')
plt.scatter(spain.Deaths, spain.Recovered, color='black', label='Spain')

plt.xlabel('Deaths')
plt.ylabel('Recovered')
plt.title('Turkey Coronavirus Analysis')
plt.legend()

plt.show()
