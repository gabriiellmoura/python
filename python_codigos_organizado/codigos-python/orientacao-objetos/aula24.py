from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('abrindo o arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as error_:
        print ('ocorreu este erro', error_)
    finally:
        print('fechando o arquivo')
        arquivo.close()

with my_open ('aula24.txt', 'w') as arquivo:
    arquivo.write('linha 01\n')
    arquivo.write('linha 02\n')
    arquivo.write('linha 03\n')
    print('WHIT', arquivo)