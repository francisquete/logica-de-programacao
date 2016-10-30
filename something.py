#fatorial

num=int(input("numero: "))
fat = 1
i = 1

while num <= 5:
    fat += i
    i += 1
print("fatorial de %d = %d" %(num,fat))
