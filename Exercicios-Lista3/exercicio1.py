def abastecimento():
    gasolina= 5.59
    etanol = 4.39
    diesel = 5.99
    print("Qual combustível escolhido?")
    tipo_combs = str(input("1 - Gasolina, 2 - Etanoia, 3 - Vin Diesel"))
    litros = float(input("Quantos litros abastecidos?"))
    if tipo_combs == "1":
        valortotal = gasolina * litros
    elif tipo_combs == "2":
        valortotal = etanol * litros
    else:
        valortotal = diesel * litros
    print(f"O valor total do abastecimento de {litros} L de {tipo_combs} é de: R${valortotal}")

abastecimento()