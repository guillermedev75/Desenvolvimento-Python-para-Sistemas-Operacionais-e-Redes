import threading
import random
import time

tamanho_vetor = int(input('Qual o tamanho do vetor: '))
vetor_a = []
vetor_n = []
lista_de_threads = []
total_threads = 4


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)


def fatoracao(lista_vetor_a, start, end):
    for i in lista_vetor_a[start:end]:
        resultado_fatoracao = fatorial(i)
        vetor_n.append(resultado_fatoracao)


inicio_monitoramento = float(time.time())

for i in range(tamanho_vetor):
    vetor_a.append(random.randint(0, tamanho_vetor))

tamanho_a = len(vetor_a)

for i in range(total_threads):
    start = i * int(tamanho_a/total_threads)
    end = (i + 1) * int(tamanho_a/total_threads)
    thread = threading.Thread(target=fatoracao, args=(vetor_a, start, end))
    thread.start()
    lista_de_threads.append(thread)

for thread in lista_de_threads:
    thread.join()

fim_monitoramento = float(time.time())

tempo = fim_monitoramento - inicio_monitoramento

print(f'Tempo: {tempo}')
