import numpy as np
ids, price , long , lat = np.genfromtxt('Week4/zameencom-property-data-By-Kaggle-short.csv', delimiter=';', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1)
print(ids)
print(price)
print(long)
print(lat)

print(np.min(price))
# Zameen.com price  - statistics operations
print("Zameen.com Price mean: " , np.mean(price))
print("Zameen.com Price average: " , np.average(price))
print("Zameen.com Price std: " , np.std(price))
print("Zameen.com Price mod: " , np.median(price))
print("Zameen.com Price percentile - 25: " , np.percentile(price,25))
print("Zameen.com Price percentile  - 75: " , np.percentile(price,75))
print("Zameen.com Price percentile  - 3: " , np.percentile(price,3))
print("Zameen.com Price min : " , np.min(price))
print("Zameen.com Price max : " , np.max(price))
# Zameen.com price  - maths operations
print("Zameen.com Price square: " , np.square(price))
print("Zameen.com Price sqrt: " , np.sqrt(price))
print("Zameen.com Price pow: " , np.power(price,price))
print("Zameen.com Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat

print(" Zameen.com Long - lat - Addition:", addition)
print(" Zameen.com Long - lat - Subtraction:", subtraction)
print(" Zameen.com Long - lat - Multiplication:", multiplication)
print(" Zameen.com Long - lat - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("Zameen.com Price - div - pie  - Sine values:", sine_values)
print("Zameen.com Price - div - pie Cosine values:", cosine_values)
print("Zameen.com Price - div - pie Tangent values:", tangent_values)

print("Zameen.com Price - div - pie  - Exponential values:", np.exp(pricePie))

 Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("Zameen.com Price - div - pie  - Natural logarithm values:", log_array)
print("Zameen.com Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("Zameen.com Price - div - pie   -Hyperbolic Tangent values:", tanh_values)




































