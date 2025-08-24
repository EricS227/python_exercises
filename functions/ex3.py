# Escreva uma função que recebe dois inteiros e retorna o MDC

def calc_mdc(n1, n2):
    temp = 0
    while n2 != 0:
        temp = n2
        n2  = n1 % n2
        n1 = temp
    return n1
    

print(calc_mdc(6,12))
    

        