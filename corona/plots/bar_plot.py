import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')

turkey = dataset[dataset['Country/Region'] == 'Turkey']

plt.bar(turkey.Deaths, turkey.Recovered)
plt.xlabel('Deaths')
plt.ylabel('Recovered')
plt.title('Turkey Coronavirus Analysis')
plt.show()
