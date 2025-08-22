#Leia a nota de um aluno e imprima "Aprovado" se for maior ou igual a 7, senão "Reprovado"


notas = float(input("Digite a sua nota: "))

if notas < 7.0:
    print("Está reprovado")
else:
    print("Está aprovado")