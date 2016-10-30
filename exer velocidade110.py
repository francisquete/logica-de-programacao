velo = int(input("digite a velocidade do seu carro em km/h: "))
multa = (velo - 110) * 5

if velo > 110:
    print("você ultrapassou o limite de velocidade e tera que pagar uma multa")
    print("o valor da multa é de %d reais" %multa)
else:
    print("esta tudo ok com voce")
