import numpy as np

status,price,bed,bath = np.genfromtxt('Mycsvfile/RealEstate-USA (1).csv',delimiter=',',usecols=(1,2,3,4),unpack=True,dtype=None,skip_header=1)

print(status)
print(price)
print(bed)
print(bath)

# Statistic opration
print("RealEstate price means:", np.mean(price))
print("RealEstate price avrage:", np.average(price))
print("RealEstate price standerddiviation:", np.std(price))
print("RealEstate price median:", np.median(price))
print("RealEstate price percentile-25:", np.percentile(price,25))
print("RealEstate price percentile-75:", np.percentile(price,75))
print("RealEstate price percentile-3:", np.percentile(price,3))
print("RealEstate price min:", np.min(price))
print("RealEstate price max:", np.max(price))

# math opration
print("RealEstae price squre:",np.square(price))
print("RealEstate price sqrt:",np.sqrt(price))
print("RealEstate price power",np.power(price,price))
print("RealEstate price abs:",np.abs(price))

# Basic Arithmatic opration
addition = bed + bath
print("RealEstate addition of bed and bath:",addition)
substraction = bed - bath
print("RealEstate subtruction of bed and bath:",substraction)
multiplication = bed * bath
print("RealEstate multiplication of bed and bath:",multiplication)
divition = bed - bath
print("RealEstate divition of bed and bath:",divition)

# Trignomatric function
pricepie = (price/np.pi) +1
# calculate sin cosin tangent
sin_value = np.sin(pricepie)
cosine_value = np.cos(pricepie)
tangent_value = np.tan(pricepie)
print("the sin value of pricepie:",sin_value)
print("the cosin value of pricepie:",cosine_value)
print("the tangent value of pricepie:",tangent_value)
print("the expotential value:",np.exp(pricepie))

# Natural algorithm and base10
log_array = np.log(pricepie)
print("the value of natural log:",log_array)
log10_array = np.log10(pricepie)
print("the value of base10 log:",log10_array)

# Hyperbolic sin ,cosin,tangent
sinh_value = np.sinh(pricepie)
print("the hyperbolic sinh value:",sinh_value)
cosh_value = np.cosh(pricepie)
print("the hyperbolic cosh value:",cosh_value)
tanh_value = np.tanh(pricepie)
print("the hyperbolic tanh value:",tanh_value)

# invers hyperbolic sin,cosin,tangent
asinh_value = np.asinh(pricepie)
print("the hyperbolic inverse value of sin:",asinh_value)
acosh_value = np.acosh(pricepie)
print("the hyperbolic inverse value of cos:",acosh_value)

# Realestate bed + bath 2demintional array
D2bedbath = np.array([bed,bath])
print("Realestate bed bath 2demetional array:",D2bedbath)

# check the demention of array
print("RealEate bed bath array demention:",D2bedbath.ndim)

#print total number of element in the arraY
print("The total number of array:",D2bedbath.size)

#Return the tuple of array
print("2demention array gives the size of array inthe each dementon:",D2bedbath.shape)

# check the data type of array
print("RealEstate bed bath 2dementional array data type:",D2bedbath.dtype)

#slicing array
D2bedbathslice = D2bedbath[:1,:5]
print("RealEstate splice an array:",D2bedbathslice)
D2bedbathslice2 = D2bedbath[:1,4:15:4]
print("the splicing of array:",D2bedbathslice2)

#indexing of array
D2bedbathsliceitemonly = D2bedbath[0:1]
print("indexing the value of array:",D2bedbathsliceitemonly)
D2bedbathslice2itemonly = D2bedbath[1:2]
print("the indexing value of array:",D2bedbathslice2itemonly)

#use the builtin function if you don't have to need od indexes so use the nditer

for elem  in np.nditer(D2bedbath):
    print(elem)

#if you have need indexes then

for index,elem in np.ndenumerate(D2bedbath):
    print(index,elem)

# Reshape the array
    D2bedbath1To400 = np.reshape(D2bedbath,(1,400))
    print("the reshape of an array:",D2bedbath1To400)
    print("the size of reshape array:",D2bedbath1To400.size)
    print("the demention of the array:",D2bedbath1To400.ndim)
    print("the shape of the array:",D2bedbath1To400.shape)
    print("the demention of the array:",D2bedbath1To400.ndim)
     