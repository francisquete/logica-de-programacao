#peça uma nota de 0 a 10, mostre uma mensagem caso o valor seja invalido e continue pedindo
#até que o usuario informe um valor valido


nota = int(input("uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("erro")
    nota = int(input("digite uma nota entre 0 e 10: "))
