# Escreva uma função que recebe uma lista de números e retorna a média deles
lisuto = []

for i in range(6+1):
    numeros = int(input("Digite um numero: "))
    lisuto.append(numeros)


def calc_media(lista):
    soma = 0
    for i in lista:
        soma +=i
    
    avg = soma / len(lista)

    return avg


calc_media(lisuto)
print(calc_media(lisuto))