#Leia uma string e conte quantas vogais existem nela

vogais = 0

string = str(input("Digite uma string: "))

for i in string.lower():
    if i in "aeiou":
        vogais += 1

print(f'{string} tem  {vogais} vogais')