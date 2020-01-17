import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

string_data

print(string_data)

print(string_data.isnull())

string_data[0] = None

print(string_data.isnull())

print(string_data.notnull())

from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])

print(data.dropna())

data = pd.Series([1, NA,3.5, NA, 7])

print(data.notnull())

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

print(data)

print(cleaned)

data.dropna(how='all')
