list = [int(x) for x in input().split()]
v=0
for i in range(len(list)):
    if list[i] > 0:
        v += list[i]

if v == 0:
    v = min(list)
print(v)