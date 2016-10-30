#verifique se a palavra é palindrome (igual de tras para frente)

palavra = input("digite uma palavra: ")

if palavra [::-1] == palavra:
    print("esta palavra é palindrome")
else:
    print("palavra não palindrome")
