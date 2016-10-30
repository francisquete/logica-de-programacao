#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em m² da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 m² e que a tinta é vendida
#em latas de 18L, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

metros = int(input("metros: "))
if metros % 54 != 0:
    latas = int(metros/54) + 1
else:
    latas = metros / 54

valor = latas * 80

print("%d latas necessarias a r$: %.2f" %(latas,valor))
