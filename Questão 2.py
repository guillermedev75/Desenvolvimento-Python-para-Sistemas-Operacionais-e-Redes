import os

diretorio = input('Digite o diretório: ')
arquivo = input('Digite o nome do arquivo: ')


def abre_arquivo():
    try:
        os.startfile(os.path.join(diretorio, arquivo))
        print(f'{arquivo} foi aberto!')
    except Exception:
        print('Não foi possível abrir o arquivo!')


abre_arquivo()
