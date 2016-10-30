#fatorial

i = 1
fat = 1
n=int(input("numero: "))

while i  <= n:
    fat *= i
    i += 1
print("fat = %d" %fat)
