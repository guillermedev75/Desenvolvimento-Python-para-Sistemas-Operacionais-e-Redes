lista = []


def leitura_arquivo():
    try:
        with open('arquivo.txt', 'r', encoding='utf-8', newline='\r\n') as arquivo:
            for linha in arquivo:
                texto = linha[::-1].strip()
                lista.append(texto)
        lista.sort(reverse=True)
        return lista
    except Exception:
        print('O arquivo não foi encontrado.')


def resultado():
    for i in lista:
        print(i)


leitura_arquivo()
resultado()
