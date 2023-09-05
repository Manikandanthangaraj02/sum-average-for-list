a=[]
print("Enter ten numbers")
for i in range(10):
    b=int(input("Enter the number:"+str(i+1)))
    a.append(b)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
d=sum/10
print(d)

