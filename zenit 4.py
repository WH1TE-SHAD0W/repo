t= int(input())
a =[]
horsie = 0
lepsie = 0
vlna = 0
for i in range(t):
    a.append(int(input()))

for i in range(t-1):
    if a[(i+1)] > a[i]:
        horsie += 1
        #print(',')
    elif a[(i+1)] < a[i]:
            #print('.',a[(i+1)])
            lepsie += 1
    if a[i] > a[(i+1)] and a[i] > a[(i-1)] and i>=2 :
        vlna += 1
        #print('#',a[i])


print(lepsie, horsie, vlna)