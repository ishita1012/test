m1=float(input("enter marks of test 1"))
m2=float(input("enter marks of test 1"))
m3=float(input("enter marks of test 1"))
marks=list(m1,m2,m3)
sum=0
#find lowest
min=m1
for i in marks:
    if i<min:
        min=i
marks.remove(min)
for i in marks:
    sum+=i
avg=sum/2
print(avg)
