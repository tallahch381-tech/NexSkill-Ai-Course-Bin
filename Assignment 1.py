s= input("hellow world:")
print("Length=",len(s))

s=input("python3")
print("Upper case:",s.upper())
print("Lower case:",s.lower())

s= ("banana:")
ch=("a")
print("count=",s.count(ch))

s=("drawer:")
if s=="":
    print("empty string")
else:
    print("drawer:",s[0])    
    print("drawer:",s[-1])

    s=("data science:")
    sub=("science:")
    print(sub in s)

    s=("progrmming:")
    start=int(input(3))
    end=int(input(3))
    print(s[start:end])

    s=("python:")
    print(s[::-1])

    s=("i love apples :")
    old=("apples:")
    new=("orange:")
    print(s.replace(old,new))

    s=("split this sentence:")
    word=s.split()
    print("-".join(word))

    s=("padded text:")
    print(s.strip())
    