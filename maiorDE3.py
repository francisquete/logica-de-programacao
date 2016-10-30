#Faça um Programa que leia três números e mostre o maior deles

num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))
num3 = int(input("terceiro numero: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
else:
    print("nao pode ter valores iguais")
