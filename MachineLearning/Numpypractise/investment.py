import numpy as np

FundingRounds,InvestmentAmount,Valuation,Numberofivester = np.genfromtxt('Mycsvfile/startup_growth_investment_data (1).csv',delimiter=',',unpack=True,usecols=(2,3,4,5),dtype=None,skip_header=1)

print(FundingRounds)
print(InvestmentAmount)
print(Valuation)
print(Numberofivester)

#Statistic opration
print("The means of fundingrounds is:",np.mean(FundingRounds))
print("the standarddeviation of fundinround is:",np.std(FundingRounds))
print("the median of fundingrounds is:",np.median(FundingRounds))
print("the avrage of funding rounds is:",np.average(FundingRounds))
print("the percentile_25 of funding rounds is:",np.percentile(FundingRounds,25))
print("the percentile_75 of funding rounds is:",np.percentile(FundingRounds,75))
print("the percentile_3 of funding ruonds is:",np.percentile(FundingRounds,3))
print("the min of funding round is:",np.min(FundingRounds))
print("the max of funding riunds is:",np.max(FundingRounds))

# startup grouth investment data math opration
print("the squre of the funding round is:",np.square(FundingRounds))
print("the squre root of funding rounds is:",np.sqrt(FundingRounds))
print("the power of the funding rounds is:",np.power(FundingRounds,FundingRounds))
print("the abs of funding rounds is:",np.abs(FundingRounds))

# Basic Arithmatics opration
Addition = InvestmentAmount + Valuation
print("the addition of the investmentamount and valuation is:",Addition)
Subtraction = InvestmentAmount - Valuation
print("the subtraction of investment and valuation is:",Subtraction)
Multiplication = InvestmentAmount * Valuation
print("the multiplication of the investment and valuation is:",Multiplication)
Divition = InvestmentAmount / Valuation
print("the divition of the investment and valuation is:",Divition)

# Trignomatric function
FundingRoundspie = (FundingRounds/np.pi) +1
print("the expotential value of the funding round is:",np.exp(FundingRounds))

#calculate sin ,cosin,tangent
sin_value = np.sin(FundingRoundspie)
cosin_value = np.cos(FundingRoundspie)
tagnet_value = np.tan(FundingRoundspie)
print("the sin value of foundingroundpie is:",sin_value)
print("the cosin value of foundinroundpie is :",cosin_value)
print("the tangent vale of fundingroundspie is:",tagnet_value)

#calculate the natural log and base 1o logrithm
log_array = np.log(FundingRoundspie)
log10_array = np.log10(FundingRoundspie)
print("the natural log of the fundinround is",log_array)
print("the base10 log of the funding round is:",log10_array)

# Hyperbolic sin ,cos,tan
sinh_value = np.sinh(FundingRoundspie)
cosh_value = np.cosh(FundingRoundspie)
tanh_value = np.tanh(FundingRoundspie)
print("the hyperbolic sin value of fundingrounds is:",sinh_value)
print("the hyperbolic cos value of fundingrounds is:",cosh_value)
print("the hyperbolic tan value of fundingrouns is:",tanh_value)

# Inverse hyperbolic sin cos tan
asinh_value = np.asinh(FundingRoundspie)
acosh_value = np.acosh(FundingRoundspie)
atanh_value = np.atanh(FundingRoundspie)
print("the inverse hyperbolic sin value of fundingrounds is:",asinh_value)
print("the inverse hyperbolic cos value of fundinground is:",acosh_value)
print("the inverse hyperbolic tan value of fundinground is:",atanh_value)

# 2dementional array of fundingrounds and valuation
D2Fundval = np.array([FundingRounds,Valuation])
print("the 2dementional array of fundingrouds and valuation is:",D2Fundval)

# check the demention of the array
print("the demention of the array is:",D2Fundval.ndim)

# print total number of element
print("the total number of element in the array :",D2Fundval.size)

# return the tuple thath give the  size of each demention
print("the size of array in each demention:",D2Fundval.shape)

# check the dtype of the array
print("the data type of the array is:",D2Fundval.dtype)

# slicing of array
D2Fundvalslice = D2Fundval[:1,:5]
print("the splice of array is:",D2Fundvalslice)
D2Fundvalslice2 = D2Fundval[:1,4:15:5]
print("the slice of an array is:",D2Fundvalslice2)

#indexin the array
D2Fundvalsliceitem = D2Fundval[0:1]
print("the indexing value of an array is:",D2Fundvalsliceitem)
D2Fundvalsliceitem2 = D2Fundval[1:2]
print("the indexing value of array:",D2Fundvalsliceitem2)

# use the built in function if you have not need of index  use nditer
for elem in np.nditer(D2Fundval):
    print(elem)

# if you have need of index
for index,elem in np.ndenumerate(D2Fundval):
    print(index,elem)

# Reshape the arayy
D2Fundval1To10000 = np.reshape(D2Fundval,(1,10000))
print("the reshape array is:",D2Fundval1To10000)
print("the size of reshape array is:",D2Fundval1To10000.size)
print("the demention of reshape array is:",D2Fundval1To10000.ndim)
print("the shape of the array is:",D2Fundval1To10000.shape)