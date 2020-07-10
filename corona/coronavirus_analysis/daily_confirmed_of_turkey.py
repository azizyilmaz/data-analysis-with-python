import pandas
import matplotlib.pyplot as plt

# [1 rows x 153 columns]
dataset = pandas.read_csv(
    'corona/coronavirusdata/time_series_covid_19_confirmed_turkey.csv')

# Hide column
dataset = dataset.drop('Province/State', axis=1)
dataset = dataset.drop('Country/Region', axis=1)

# Swap rows and columns
# [153 rows x 1 columns]
dataset = dataset.T

# Add header row to a pandas DataFrame
dataset.columns = ['Confirmed']

# Filter greater than zero
dataset = dataset[dataset['Confirmed'] > 0]
print(dataset)
print(dataset.dtypes)

# Set index as datetime
dataset.index = pandas.to_datetime(dataset.index)
print(dataset)
print(dataset.dtypes)

dataset.plot(color='orange')

plt.grid()
plt.xlabel('Date')
plt.ylabel('Confirmed')
plt.title('Turkey Coronavirus Analysis')
plt.legend()
plt.show()