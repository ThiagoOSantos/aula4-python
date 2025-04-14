'''Continuação de extruturas de repetição com (Do - while) & (while)'''
def solicitar_idade():
    while True: #inicio do loop condicional - enquanto for verdade
        idade = int(input("Digite sua idade: ")) # condição de repetição
        
        if idade >= 0 and idade <= 120:
            print("Idade registrada: ", idade)
            break #estrutura que indica condição de parada
        else:
            print("Idade Inválida. Tente novamente")

'''solicitar_idade()''' #chamada de função 

def menu_simples():
    opcao = ""
    while opcao != "3":
        print("Ver mensagens ")
        print(" 2 - Repetir Menu ")
        print(" Sair")
        opcao = input("Escolha uma opção: \n " )

        if opcao == "1":
            print("Você escolheu ver a primeira mensagem!")
        elif opcao == "2":
            print("Você escolheu ver a segunda mensagem")
        elif opcao != "3":
            print("Opção inválida!")
    print("Programa encerrado. Até a próxima xD")

menu_simples()