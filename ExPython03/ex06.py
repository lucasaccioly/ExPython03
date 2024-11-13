valor = int(input("Digite um valor inteiro de 0 a 10: "))
if valor < 0 or valor > 10:
    print("Valor inválido. Por favor, insira um valor entre 0 e 10.")
else:
    print(f"Tabuada de {valor}:")
    for i in range(11):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")
        