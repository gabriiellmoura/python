from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int



if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    #p3 = p1 == p2
    print(p1 == p2)