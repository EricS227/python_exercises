# Escreva uma função que recebe uma string e retorna se ela eé palíndromo ou não


stri = input("Digite uma string: ")

def verificar_palindromo(string):
    if string == string[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

verificar_palindromo(stri)