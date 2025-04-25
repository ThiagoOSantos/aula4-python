def numaleatorio():
    alea = 6
    contagem = 0
    while True:
        opcao = int(input("Qual o número secreto do programa?"))
        if opcao == alea:
            print("Parabéns, você é phoda!")
            break
        elif opcao >alea:
            print("Maior que o número")
        else:
            print("Menor que o numero")
        contagem += 1
        if contagem == 3:
            print("Suas chances acabaram")
            break
numaleatorio()