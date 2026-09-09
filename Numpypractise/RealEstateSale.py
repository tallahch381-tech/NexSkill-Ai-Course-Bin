import numpy as np

SerialNumber,SaleAmount,AssessedValue,SalesRatio = np.genfromtxt('Mycsvfile/Real_Estate_Sales_2001-2022_GL-Short (1).csv',invalid_raise=False,delimiter=',',unpack=True,usecols=(0,5,6,7),dtype=None,skip_header=1)

print(SerialNumber)
print(SaleAmount)
print(AssessedValue)
print(SalesRatio)

# Statistic opration
print("the means of saleamount is:",np.mean(SaleAmount))
print("the avrage of saleamuont is:",np.average(SaleAmount))
print("the standarddeveation of Saleamount is:",np.std(SaleAmount))
print("the median of the saleamount is:",np.median(SaleAmount))
print("the percentile_25 of Saleamount is:",np.percentile(SaleAmount,25))
print("the percentile_75 of saleamount is:",np.percentile(SaleAmount,75))
print("the percentile_3 of saleamount is :",np.percentile(SaleAmount,3))
print("the min of the saleamount is:",np.min(SaleAmount))
print("the max of the saleamount is:",np.max(SaleAmount))

# Math opration
print("the squre of the saleamount is:",np.square(SaleAmount))
print("the squrer root of the saleamount is:",np.sqrt(SaleAmount))
print("the power of the saleamount is:",np.power(SaleAmount,SaleAmount))
print("the abs of the saleamount is:",np.abs(SaleAmount))

# basic arithmatic opration
Addition = SerialNumber + AssessedValue
subtracton = SerialNumber - AssessedValue
multiplication = SerialNumber * AssessedValue
Divition = SerialNumber / AssessedValue
print("the addition of the serialnumber and assessedvalue is:",Addition)
print("the subtraction of the serialnumber and assessedvalue is :",subtracton)
print("th multiplication of the serialnumer and assessedvalue is:",multiplication)
print("the divition of the serialnumber and assessedvalue is:",Divition)

# Trignomatric function
SaleAmountpie = (SaleAmount/np.pi) +1
print("the expotantial value of Saleamount is:",np.exp(SaleAmountpie))

# calculate the sin cosin  and tangent
sin_value = np.sin(SaleAmountpie)
cosin_value = np.cos(SaleAmountpie)
tangent_value = np.tan(SaleAmountpie)
print("the sin_value of the saleamount is:",sin_value)
print("the cosin_value of the saleamount is:",cosin_value)
print("the tangent value of saleamount is:",tangent_value)

#calculate the hyperbolic sin cos and tan
sinh_value = np.sinh(SaleAmountpie)
cosh_value = np.cosh(SaleAmountpie)
tanh_value = np.tanh(SaleAmountpie)
print("the sinh value of the saleamount is:",sinh_value)
print("the cosh value of saleamount is:",cosh_value)
print("the tanh value of the saleamount is: ",tanh_value)

#calculate the hyperbolic inverse of sin ,cos tan
asinh_value = np.asinh(SaleAmountpie)
acosh_value = np.acosh(SaleAmountpie)
atanh_value = np.atanh(SaleAmountpie)
print("the asinh value of the saleamount is:",asinh_value)
print("the acosh value of the saleamount is :",acosh_value)
print("the atanh value of the saleamount is:",atanh_value)

# 2dementional array of serialnumber and saleratio
D2SerialSale = np.array([SerialNumber,SalesRatio])
print("the 2dementional array of serialnumber and saleratio is:",D2SerialSale)

# check the total number of element in the array
print("the total number of element in the array is:",D2SerialSale.size)

# the demention of the array
print("the demention of the array is:",D2SerialSale.ndim)

# the shape of the array in the form of the tuple
print("the shape of the array is:",D2SerialSale.shape)

# check the dtype of the array is
print("the data type of the array is:",D2SerialSale.dtype)

# slicing the array
D2SerialSaleslice = D2SerialSale[:1,:5]
print("the slice of the array is:",D2SerialSaleslice)
D2SerialSaleslice2 = D2SerialSale[:1,4:15:5]
print("the slice of an array is:",D2SerialSaleslice2)

# indexing the array
D2SerialSaleitem = D2SerialSale[0:1]
print("the index of the array is :",D2SerialSaleitem)
D2SerialSaleitem2 = D2SerialSale[1:2]
print("the index of the array is:",D2SerialSaleitem2)

# you should use the built in function if yo have don't need of index value us enditer
for elem in np.nditer(D2SerialSale) :
    print(elem)

#if you have need to index use ndenumerate
for index,elem in np.ndenumerate(D2SerialSale) :
    print(index,elem)

# reshape the array 1,278
D2SerialSale1To278 = np.reshape(D2SerialSale,(1,278))
print("the size of the arry is:",D2SerialSale1To278.size)
print("the demention of the array is:",D2SerialSale1To278.ndim)
print("the shape of the array is:",D2SerialSale1To278.shape)