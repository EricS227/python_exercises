#leia uma lista de numeros e imprima o maior e o menor valor

lisuto = []


for i in range(6):
    num = int(input("Digite o numero: "))
    lisuto.append(num)


maior = lisuto[0]
menor = lisuto[0]

for num in lisuto:
    if num > maior:
        maior = num
    elif num < maior:
        menor = num

print("O maior é", maior, "E o menor é: ", menor)