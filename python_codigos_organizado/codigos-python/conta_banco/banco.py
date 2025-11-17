import contas
import pessoas

class Banco:
    def __init__(
        self,
        agencias: list[int] | None= None,
        clientes: list[pessoas.Pessoa] | None= None,
        contas: list[contas.Conta] | None= None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_conta_cliente', True)
            return True
        print('_checa_conta_cliente', False)
        return False
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
    
if __name__ == '__main__':
    cliente01 = pessoas.Cliente('Gabriel', 23)
    conta_corrente = contas.ContaCorrente(111, 222, 0, 0)
    cliente01.conta = conta_corrente
    banco = Banco()
    banco.clientes.extend([cliente01])
    banco.contas.extend([conta_corrente])
    banco.agencias.extend([111])
    
    
    if banco.autenticar(cliente01, conta_corrente):
        conta_corrente.depositar(10)
        cliente01.conta.depositar(100)
        print(cliente01.conta)