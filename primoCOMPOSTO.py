#decomposicao primos

n = int(input("numero: "))
for k in range (2, n):
    while n % k == 0:
        print(k)
        n = n / k
