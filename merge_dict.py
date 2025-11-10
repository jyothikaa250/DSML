items1=input("enter the keyvalues  seperated by spaces: ").split()
items2=input("enter the keyvalues  seperated by spaces: ").split()
t1=[(items1[i],items1[i+1]) for i in range(0,len(items1),2)]
t2=[(items2[j],items2[j+1]) for j in range(0,len(items2),2)]
d1=dict(t1)
d2=dict(t2)
m=d1.copy()
m.update(d2)
print("merged dictionary",m)