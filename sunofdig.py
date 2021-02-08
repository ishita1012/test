while True:
    N= input("enter a 4 digit number: ")
    if N.isnumeric()==True and len(N)==4:
        break;

sum=0
for i in N:
    sum+=int(i)
print(sum)
