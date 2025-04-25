#exercicio 5 
'''
def relogio_digital():
    horas_limite= int(input("Digite o numero de horas para simular: \n"))

    for hora in range(horas_limite):
        for minuto in range (60):
            for segundo in range (60):
                print(f"{hora:02d}:{minuto:02d}:{segundo:02d}") #o 02d serve para definir 2 casas decimais em python

relogio_digital()
'''
#exercicio 9 


#exercicio 10

def analisador_palavras():
    for i in range(3):
        palavra = input("Digite a palavra para ser analisada:\n")
        vogais = 0
        consoantes = 0
        espacos = 0
        for letra in palavra.lower():
            if letra in "aeiou":
                vogais += 1
            elif letra == " ":
                espacos += 1
            elif letra.isalpha():
                consoantes += 1
        print(f"O resultado da {palavra} é:\n")
        print("Vogais: ", vogais)
        print("Espaços: ", espacos)
        print("Consoantes: ", consoantes)

analisador_palavras()