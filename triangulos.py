#Faça um Programa que peça os três lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

a = int(input("primeiro lado: "))
b= int(input("segundo lado: "))
c = int(input("terceiro lado: "))

if a == 0 or b == 0 or c == 0:
    print("Não e triangulo")
elif a == b or a == c or b == c:
    print("triangulo isosceles")
elif a != b and a != c and b !=c:
    print("triangulo escaleno")
elif a == b and a == c and b == c:
    print("triangulo equilatero")
