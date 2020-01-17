import pandas as pd
import numpy as np

data = pd.DataFrame({'k1':['one','two']*3 + ['two'], 'k2':[1,1,2,3,3,4,4]})

print(data)

print(data.duplicated())

print(data.drop_duplicates())

data['v1'] = range(7)

print(data.drop_duplicates(['k1']))

data = pd.DataFrame({'food':['bacon','pulled pork', 'bacon', 'pastrami', 'corned beef',
                           'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                     'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print(data)

print("\n")

meat_to_animal = {'bacon':'pig', 'pulled pork':'pig', 'pastrami':'cow', 'corned beef':'cow', 'honey ham':'pig', 'nova lox':'salmon'}

lowercased = data['food'].str.lower()

print(lowercased)

print(data['food'].map(lambda x: meat_to_animal[x.lower()]))
