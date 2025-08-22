#Leia três números e imprima o maior deles


lisuto = []


for i in range(3):
    num = int(input("Digite os números: "))
    lisuto.append(num)

maior = lisuto[0]

for n in lisuto:
    if n > maior:
        maior = n

print("O Maior é" , maior)        