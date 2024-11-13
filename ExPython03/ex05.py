soma = 0
contagem = 6
for i in range(contagem):
    valor = float(input("Digite o {}º valor: ".format(i + 1)))
    soma += valor
    media = soma / contagem
print("A soma dos valores é:", soma)
print("A média dos valores é:", media)