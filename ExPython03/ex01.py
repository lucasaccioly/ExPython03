n1= int(input("Digite um valor: "))
n2= int(input("Digite outro valor: "))
soma=n1+n2
print("O Resultado foi {}".format(soma))
resultado = soma % 2
if resultado == 0:
    print("O número é PAR")
else:
    print("O número é IMPAR")


