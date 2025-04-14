def ehprimo():
    primo = bool
    numero = int(input("Digite um numero para verificar se é primo"))
    while numero != 0:
        for i in range(1, numero):
            if numero % i == 0:
                primo = True
                print("É primo")
                break
            else:
                print("Não é primo, tente outro (:")
ehprimo()
            