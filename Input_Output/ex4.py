#Leia uma linha com N inteiros e imprime a soma deles

listo = []


for i in range(4):
    esc = int(input("Digite os numeros: "))
    listo.append(esc)

soma = 0
for num in listo:
    soma += num


print("Soma: ", soma)