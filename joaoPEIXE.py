#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
#o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
#um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
#Se houver, gravar na variável excesso e na variável multa o valor da multa que João deve pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.


peso = int(input("peso em kg: "))
pesoMax = 50
excesso = 0
multa = 0

if peso > pesoMax:
    excesso = peso - pesoMax
    multa = (peso - pesoMax) * 4
    print("excesso em kg: %d" %excesso)
    print("multa R$ %5.2f" %multa)
else:
    print("excesso em kg: %.2f" %excesso)
    print("multa de r$: %5.2f" %multa)
