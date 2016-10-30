minutos = int(input("minutos falados: "))

if minutos <= 5:
    preco = minutos *2
elif minutos > 5 and minutos <= 10:
    preco = minutos * 5
else:
    preco = minutos * 10

print("o valor da sua conta e de: %5.2f" %preco, "reais")
