#numero primo

n = int(input("numero: "))
k = 1
divisor = 0
while k <= n:
    if n % k == 0:
        divisor += 1
    k += 1
print(divisor == 2)
