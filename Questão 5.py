lista_a = []
lista_b = []
soma_total = []

def leitura_arquivo():
    try:
        with open('a.txt', 'r') as txt_a:
            for i in txt_a.readlines():
                txt_a = i.split(' ')
        for numero in txt_a:
            lista_a.append(int(numero))

        with open('b.txt', 'r') as txt_b:
            for i in txt_b.readlines():
                txt_b = i.split(' ')
        for numero in txt_b:
            lista_b.append(int(numero))
    except Exception:
        print('O arquivo não foi encontrado')


def verificador():
    tamanho_a = len(lista_a)
    tamanho_b = len(lista_b)
    diferenca = tamanho_a - tamanho_b

    if diferenca > 0:
        for i in range(0, abs(diferenca)):
            lista_b.append(0)
    elif diferenca < 0:
        for i in range(0, abs(diferenca)):
            lista_a.append(0)
    else:
        pass
    for a, b in zip(lista_a, lista_b):
        soma_total.append(sum([a, b]))

def resultado():
    for soma in soma_total:
        print('{}{:<7}'.format(' '*2, soma))


leitura_arquivo()
verificador()
resultado()
