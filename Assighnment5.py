# Question 1:
# Write a program that converts a temperature from Celsius to Fahrenheit.

celsius = float(input("9/5: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Question 2:
# Calculate Area of a Rectangle

length = float(input("5m: "))
width = float(input("4m: "))

area = length * width

print("Area of Rectangle:", area)

# Question 3:
# Calculate Compound Interest

principal = float(input("calculatecompound interest: "))
rate = float(input("45 (%): "))
time = float(input("22 (years): "))

ci = principal * (1 + rate/100) ** time - principal

print("Compound Interest:", ci)

# Question 4:
# Calculate Perimeter of a Rectangle

length = float(input("4m: "))
width = float(input("4m: "))

perimeter = 2 * (length + width)

print("Perimeter:", perimeter)

# Question 5:
# Average of Three Numbers

a = float(input("45: "))
b = float(input("44: "))
c = float(input("43: "))

average = (a + b + c) / 3

print("Average:", average)

# Question 6:
# Square and Cube of a Number

num = float(input("56: "))

print("Square:", num ** 2)
print("Cube:", num ** 3)

# Question 7:
# Distribute Items Equally

candies = int(input("55: "))
students = int(input("25: "))

each = candies // students
left = candies % students

print("2:", each)
print("5:", left)

# Question 8:
# Calculate Profit or Loss

cost = float(input("5000: "))
sell = float(input("6000: "))

if sell > cost:
    print("1000 =", sell - cost)
elif cost > sell:
    print("no loss=", 5000 -6000)
else:
    print("profit")

    # Question 9:
# Total Marks and Percentage

m1 = float(input("55: "))
m2 = float(input("65: "))
m3 = float(input("45: "))
m4 = float(input("76: "))
m5 = float(input("66: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
average = total / 5

print("500", total)
print("25%", percentage, "%")
print("45%", average)

# Question 10:
# Salary Calculator

basic = float(input("500000: "))

hra = basic * 0.20
da = basic * 0.15
total = basic + hra + da

print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total)

# Question 11:
# Age in Months and Days

age = int(input("16 Years: "))

months = age * 12
days = age * 365

print("Age in Months:", months)
print("Age in Days:", days)

# Question 12:
# Currency Converter

usd = float(input("6: "))

rate = 285

pkr = usd * rate

print("Amount in PKR:", pkr)

# Question 13:
# Sum of First N Natural Numbers

n = int(input("55: "))

sum = n * (n + 1) / 2

print("Sum =", sum)

# Question 14:
# Percentage of Correct Answers

total = int(input("55: "))
correct = int(input("45: "))

percentage = (correct / total) * 100

print("Percentage:", percentage, "%")

# Question 15:
# Speed, Distance and Time

distance = float(input("77km: "))
time = float(input("2 hours: "))

speed = distance / time

print("Speed:", speed)

# Question 16:
# Calculate BMI

weight = float(input("55 (kg): "))
height = float(input("1.75 (m): "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

# Question 17:
# Convert Minutes to Hours and Minutes

minutes = int(input("55minutes: "))

hours = minutes // 60
remaining = minutes % 60

print(hours, "hours", remaining, "minutes")