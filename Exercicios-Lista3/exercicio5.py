def horacontada():
    while True:
        hora= int(input("Que horas devemos fazer a contagem?"))
        for i in range(hora):
            contaminuto = (hora) * 60
            contasegundos = (contaminuto)*60
        print(f"A contagem simulada é de: {hora}:{contaminuto:02d} e {contasegundos:02d}")

horacontada()
