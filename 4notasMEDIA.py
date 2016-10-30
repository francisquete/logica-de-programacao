#ler 4 notras, mostre-as e calcule a media

notas = []
soma = 0
i = 1
while i <=4:
    n=int(input("nota: "))
    notas.append(n)
    soma += n
    i += 1
print("notas: ",notas)
print("media: %4.2f" %(soma/4))
