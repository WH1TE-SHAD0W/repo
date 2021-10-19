t= int(input())
a =[]
horsie = 0
lepsie = 0
vlna = 0
for i in range(t):
    a.append(int(input()))

for i in range(t-1):
    if i <= t:
        if a[i] > a[i-1]:
            horsie += 1
        elif a[i] > a[i+1]:
            lepsie += 1
    if a[i] > a[i+1] and a[i] > a[i-1]:
        vlna += 1


print(lepsie, horsie, vlna)