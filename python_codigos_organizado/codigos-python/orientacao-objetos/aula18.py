# Polimorfismo em python orientado a obejtos
from abc import ABC, abstractmethod
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('email enviando', self.mensagem)
        return False
    
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS enviando', self.mensagem)
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('notificacao enviada')
    else:
        print('notificacao nao enviada')

notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)