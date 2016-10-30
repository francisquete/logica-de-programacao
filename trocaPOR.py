#ler palavra e trocar as vogais por "*"

palavra = input("palavra: ")
x = 0
troca = ""

while x < len(palavra):
    if palavra[x] in 'aeiou':
        troca = troca + "*"
    else:
        troca = troca + palavra[x]
    x += 1
print("palavra com substituições: %s" %troca)
