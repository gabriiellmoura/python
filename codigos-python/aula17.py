from abc import ABC, abstractmethod

class abstracyFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

class Foo(abstracyFoo):
    def __init__(self, name):
        super().__init__(name)

    @abstracyFoo.name.setter
    def name(self, name):
        self._name = name

foo = Foo('bar')
print(foo.name)