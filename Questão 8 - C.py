import multiprocessing
import time
import random

vetor_b = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calcula_fatorial(num1, num2):
    fat_lista = num1.get()
    vetores = []
    for item in fat_lista:
        fat = fatorial(item)
        vetores.append(fat)
    num2.put(vetores)


if __name__ == '__main__':
    tam_vetor = int(input('De 0 a 20, qual o vetor? '))
    inicio_tempo = float(time.time())

    vetor_a = []
    for i in range(tam_vetor):
        vetor_a.append(random.randint(0, 20))

    num_processamento = 4

    na_fila = multiprocessing.Queue()
    fora_da_fila = multiprocessing.Queue()

    lista_processo = []
    for i in range(num_processamento):
        inicio = i * int(tam_vetor/num_processamento)
        fim = (i + 1) * int(tam_vetor/num_processamento)
        na_fila.put(vetor_a[inicio:fim])
        multipro = multiprocessing.Process(target=calcula_fatorial, args=(na_fila,
                                                           fora_da_fila))
        multipro.start()
        lista_processo.append(multipro)

    for multipro in lista_processo:
        multipro.join()

    for i in range(0, num_processamento):
        for item in fora_da_fila.get():
            vetor_b.append(item)

    print(vetor_b)
