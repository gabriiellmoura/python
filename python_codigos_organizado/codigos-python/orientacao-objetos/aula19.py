class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    raise exception_

try:
    levantar()
except (MeuError) as error:
    print(error) # isso python retorna em args
    exception_ = OutroError('qualquer coisa')