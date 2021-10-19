t= int(input())
a =[]
for i in range(t):
    a.append(int(input()))

def Digits(n):

    minimum = 9

    while (n):
        r = n % 10

        minimum = min(r, minimum)

        n = n // 10

    print(minimum)

for i in range(t):
    if a[i] != 0:
        Digits(a[i])
    else:
        print(0)