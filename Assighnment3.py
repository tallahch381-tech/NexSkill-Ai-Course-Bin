SQUARES=[ x**2 for x in range(21)if x%2 ==0]
print(SQUARES)

nums=[3,1,4,1,5,9]
sorted_nums= sorted(nums)
print("original:",nums)
print("sorted:",sorted_nums)

nums=[1,2,2,3,1,4,5]
unique=[]
for x in nums:
    if x not in unique:
        unique.append(x)
print(unique)

nested=[[1,2],[3,4],[5]]
flat=[item for sublist in nested for item in sublist]
print(flat)

names=['alice','Bob','charlie','David']
result=sorted(names,key=str .lower)
print(result)

a=[10,20,30,40,50,60,]
a=[2.5]=[100,200]
print(a)

nums=[7,2,7,4,7,5]
indices=[i for i ,x in enumerate(nums)if x==7]
print(indices)

nums=[1,2,2,3,4,4,5]
unique=[x for x in nums if nums . count (x)==1]
print(unique)

1 = [1,2,3,4]
rotated=1[-1:]+1[:-1]
print(rotated)

nums=[1,2,3,4,5,6]
even=[x for x in nums if x %2==0]
odd=[x for x in nums if x % 2!=0]
print("even:",even)
print("odd:", odd)

numbers=[1,2,3,4]
t= tuple(numbers)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)

t=(('a',1),('b',2),('c',3))
result=[x[1]for x in t]
print(result)

def calculate(nums):
    return sum (nums),
min(nums),max (nums)
numbers=[10,20,30,40,]
total,minimum,maximum=calculate(numbers)
print("sum:",total)
print("min:",minimum)
print("max:",maximum)

t1=(1,2,3)
t2=(4,5)
result= list(t1 +t2)
print(result)

t=(1, 2, 2,3,2,4,4)
most=None
count=0
for i in set(t):
    if t.count(i)>count:
        count=t.count(i)
        most=i
print("most frequent:",most)
t1 =(3,1,2)
t2 =(2,3,1)
print (sorted(t1)==sorted(t2))

t =(10,20,30,40,50,60) 
print(t[-3:])

t=(1,2)
print(t*3)

t=((1,2),(3,4))
flat=tuple(item for sub in t for item in sub)
print(flat)

point1=(2,3)
point2=(5,7)
distance=abs(point1[0] - point2[0])+abs(point1[1]-point2[1])
print(distance)
