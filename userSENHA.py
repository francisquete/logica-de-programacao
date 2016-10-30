#leia o nome do usuario e senha e nao podem ser iguais

user = input("escolha um id: ")
senha = input("escolha uma senha: ")
while user == senha:
    print("id e senha nao podem ser iguais")
    user = input("escolha um id: ")
    senha = input("escolha uma senha: ")
else:
    print("para jogar la pelota yo necesito estar con los parças")
