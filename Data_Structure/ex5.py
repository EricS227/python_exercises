#Crie um dicionario onde as chaves são nomes de pessoas e os valores são idades. Depois, leia um nome e imprima a iddade correspondente

nomes_idade = {"Nome1": 22, "Nome2": 23, "Nome3": 34, "Nome5": 45}

name = input("Digite o nome: ")

if name in nomes_idade:
    print("A Idade de", name, "é", nomes_idade[name])
else:
    print("Esse nome não está no dicionário")