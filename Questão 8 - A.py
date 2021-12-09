vetor_A = [8, 13]
vetor_B = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def resultado():
    for i in vetor_A:
        resultado_fatoracao = fatorial(i)
        vetor_B.append(resultado_fatoracao)

    print(vetor_B)


resultado()
