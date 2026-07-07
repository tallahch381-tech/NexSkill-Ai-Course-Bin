import numpy as np
ids, price , long , lat = np.genfromtxt('Week4/zameencom-property-data-By-Kaggle-short.csv', delimiter=';', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1)
print(ids)
print(price)
print(long)
print(lat)

print()