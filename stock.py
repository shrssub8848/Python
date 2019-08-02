s=[]
while(True):
    n=int(input("enter the size of stock list "))
    if(n==0):
        print(s,"List cannot be empty \n")
    elif(n==1):
        print(s,"list cannot have only one value \n ")
    else:
        break
stock = []
for i in range(0,n):
    st=int(input("enter the values"))
    stock.append(st)
k=1
total=0
result=[]
for i in stock:
    j=k
    while j<(len(stock)):
        total=stock[j]-i
        result.append(total)
        j+=1
    k=k+1

if stock.count(stock[0]) == len(stock):
    s.append(stock[0])
    print(s)
else:
    print(result)
    s.append(max(result))
    print(s)

