#Determine se um ano é bissexto
#ano bissexto: divisivel por 4, divisivel por 100, divisivel por 400

ano = int(input("ano: "))

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("ano bissexto")
else:
    print("nao bissexto")
