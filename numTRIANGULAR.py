#NUMERO TRIANGULAR
n = int(input("n: "))
k = 0

while k * (k+1) * (k+2) < n:
    k += 1
print(k * (k+1) * (k+2) == n)
    
