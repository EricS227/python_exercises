#Leia uma lista de numeros e imprima apenas os numeros pares


listo = []

for i in range(5):
    num = int(input("Digite os numeros: "))
    listo.append(num)

even = []

for numb in listo:
    if numb % 2 == 0:
        even.append(numb)

print("Os numeros pares são: ", even)