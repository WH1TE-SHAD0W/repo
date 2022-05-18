a = []
a = input().split()
a[2]=float(a[2])
a[0]=int(a[0])
a[1]=int(a[1])
p=a[0]
for i in range(a[1]):
    if a[2] >= 0.5:
        p=p*2*a[2]
print(p)