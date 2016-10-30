#vetor de DEZ na ordem inversa (traz pra frente)

vetor = []
i = 1
while i <=10:
    n=int(input("num: "))
    vetor.append(n)
    i+=1
i=9
while i>= 0:
    print(vetor[i])
    i-=1
