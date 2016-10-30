#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês
#faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
#Calcule os descontos e o salário líquido, conforme a tabela
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

salarioHora = int(input("salario hora: "))
horasMes = int(input("horas trabalhadas no mes: "))
bruto = salarioHora * horasMes
imposto = (bruto / 100) * 11
inss = (bruto / 100) * 8
sindicato = (bruto / 100) * 5
liquido = (bruto / 100) * 76

print("salario bruto em r$: %5.2f" %bruto)
print("IR em r$: %5.2f" %imposto) 
print("INSS em r$: %5.2f" %inss)
print("sindicato em r$: %5.2f" %sindicato)
print("salario liquido em r$: %5.2f" %liquido)
