#solicite a data de nascimento (dd/mm/aaaa) e imprima com o mes por extenso

dia, mes, ano = input('data (dd/mm/aaaa): ').split('/')
meses =['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
        'outubro', 'novembro', 'dezembro']
print("voce nasce em: ")
print("%s de %s de %s" %(dia, meses[int(mes) -1], ano))
