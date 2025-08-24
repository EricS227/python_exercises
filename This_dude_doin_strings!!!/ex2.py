# Leia uma string e troque todas as vogais por *.


stri = input("Digite uma palavra: ")


string_mod = ""


for i in stri:
    if i in "aeiouAEIOU":
        string_mod += "*"
    else:
        string_mod += i

print(string_mod)