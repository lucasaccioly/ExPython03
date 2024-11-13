def categorizar_idades(idades):
    faixas_etarias = {
        "0-25 anos": 0,
        "26-60 anos": 0,
        "mais que 60 anos": 0
    }

    for idade in idades:
        if idade <= 25:
            faixas_etarias["0-25 anos"] += 1
        elif idade <= 60:
            faixas_etarias["26-60 anos"] += 1
        else:
            faixas_etarias["mais que 60 anos"] += 1

    return faixas_etarias

idades = []
continuar = True

while continuar:
    idade = int(input("Digite a idade (ou digite -1 para parar): "))
    if idade == -1:
        continuar = False
    else:
        idades.append(idade)

faixas_etarias = categorizar_idades(idades)

print("\nQuantidade de pessoas por faixa etária:")
for faixa, quantidade in faixas_etarias.items():
    print(f"{faixa}: {quantidade}")
