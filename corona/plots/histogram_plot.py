import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('corona/coronavirusdata/covid_19_data.csv')

turkey = dataset[dataset['Country/Region'] == 'Turkey']

plt.hist(turkey.Deaths, bins=10)
plt.xlabel('Deaths')
plt.ylabel('Values')
plt.title('Turkey Coronavirus Analysis')
plt.show()
