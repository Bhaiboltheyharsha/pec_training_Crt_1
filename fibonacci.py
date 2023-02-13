l=[0,1]
n=int(input("enter n"))
for i in range(n):
    s=0
    s=l[i]+l[i+1]
    l.append(s)
print(l)