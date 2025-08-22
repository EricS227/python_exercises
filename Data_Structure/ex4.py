#Leia uma lista e remova todos os elementos repetidos

Lisuto = []


for i in range(5):
    numb = int(input("Digite os numeros: "))
    Lisuto.append(numb)


No_rep = []

for num in Lisuto:
    if num not in No_rep:
        No_rep.append(num)

print("Lista original: ", Lisuto)
print("Sem repetição: ", No_rep)



#Built-in Function
#Rep = set(Lisuto)

#print(Rep)

