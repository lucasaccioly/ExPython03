numero = int(input("Digite um número : "))
if numero % 2 == 0: 
    print("Valores pares de 0 até", numero, ":")
    for i in range(0, numero + 1, 2):
        print(i, end=" ")
else:  
    print("Valores ímpares de 1 até", numero, ":")
    for i in range(1, numero + 1, 2):
        print(i, end=" ")