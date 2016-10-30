i = 1
fat = 1
n = int(input("numero: "))
while i <= n:
    fat = fat * i
    i = i + 1
print("fatorial(%d) = %d" %(n, fat))
