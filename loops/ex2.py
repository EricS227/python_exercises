#imprima todos os multiplos de 3 até 100

multiplos_3 = []

for i in range(3,101):
    if i % 3 == 0:
        multiplos_3.append(i)
    else:
        continue

print(multiplos_3)