def turmaalunos():
    opcao = ""
    nomes = []
    alunos= 0
    while opcao != "sair":
        nomes = (input("Digite o nome do aluno:\n"))
        nomes.append(nomes)
        alunos += 1
        opcao = str(input("Digite (sair) caso tenha finalizado"))
    print(f"Alunos cadastrados são: \n {nomes}")

turmaalunos()