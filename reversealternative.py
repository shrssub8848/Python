a=input("enter the string")
s= list(a)
i=0
while i<=len(a):
    s[i],s[i+1]=s[i+1],s[i]
    i+=4
a="".join(s)
print(a)