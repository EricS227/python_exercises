#leia um numero N e calcule o fatorial dele

inicial = 1

N = int(input("Digite um numero: "))

for i in range(1, N+1):
    inicial *= i

print(f"O Fatorial de {N} é {inicial}")