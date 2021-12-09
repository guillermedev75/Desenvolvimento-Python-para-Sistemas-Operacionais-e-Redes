from psutil._common import bytes2human
import os

arquivos = []
diretorio = input('Digite o caminho de um diretório: ')
os.chdir(diretorio)
listar_diretorio = os.listdir(os.chdir(diretorio))


def leitura_diretorio():
    for i in listar_diretorio:
        if os.path.isfile(os.path.join(diretorio, i)):
            arquivos.append({'name': i,
                'size': os.stat(os.path.join(diretorio, i)).st_size})

            arquivos.sort(key=lambda x: x['size'], reverse=True)

    with open('VALORES DA ESTRUTURA EM ORDEM.txt', 'w') as arquivo:
        arquivo.write(str(arquivos))


def resultado():
    print('{} {:<10} {:^10}'.format(' '*2, 'Tamanho', 'Arquivo'), sep="\n")
    for arquivo in arquivos:
        print('{} {:<10} {:^10}'.format(
            ' '*2, bytes2human(arquivo['size']), arquivo['name']))
    print('\nO arquivo gerado se encontra no diretório especificado.')


leitura_diretorio()
resultado()
