nums=[3,1,4,1,5]
print("first element:",nums[0])
print("last element:",nums[-1])

colors=['red','blue','green']
print(len(colors))

colors=['red','blue']
colors.append('yellow')
print(colors)

fruits=['apple','banana']
fruits.insert(1,'orange')
print(fruits)

fruits=['apple','banana','grapes']
fruits.remove('banana')
print(fruits)

items=[10,20,30]
x=items.pop()
print ("popped value:",x)
print(items)

nums=[1,2,3,4]
print(3 in nums)

a=[0,1,2,3,4]
print(a[2:4])
a=[5,10,15]
a[1]=12
print(a)

numbers=[1,2,2,3,2]
print(numbers.count(2))

t=(10,20,30)
print(t[1])

t=('a','b','c')
print(len(t))

x,y=(4,5)
print(x)
print(y)

t=('a','b','c')
print('b'in t)

t=()
print(type(t))

t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)

t=(7,)
print(t*3)

t=(1,2,3,2)
print(t.index(2))

t= (1,2,3,2)
print(t.count(2))

t=(5,)
print(t)
print(type(t))
