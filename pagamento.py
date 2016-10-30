#pagamento

conta = int(input('conta: '))
pagamento = int(input('pagamento: '))
troco = pagamento - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print ('uma nota de %d' %nota)
        troco -= nota
