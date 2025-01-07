import math

class Cone:
    def __init__(self, altura=0, raio=0, geratriz=0):
        self.altura = altura
        self.raio = raio
        self.geratriz = geratriz

    # Getters e Setters
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError("A altura não pode ser negativa.")
        self._altura = valor

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo.")
        self._raio = valor

    @property
    def geratriz(self):
        return self._geratriz

    @geratriz.setter
    def geratriz(self, valor):
        if valor < 0:
            raise ValueError("A geratriz não pode ser negativa.")
        self._geratriz = valor

    # Método para conferir valores desconhecidos
    def conferir(self):
        if self.geratriz == 0:
            self.geratriz = math.sqrt(self.altura**2 + self.raio**2)
        elif self.altura == 0:
            self.altura = math.sqrt(self.geratriz**2 - self.raio**2)
        elif self.raio == 0:
            self.raio = math.sqrt(self.geratriz**2 - self.altura**2)

    # Métodos de cálculo
    def area(self):
        self.conferir()  # Garante que todos os valores necessários estão preenchidos
        return math.pi * self.raio * (self.raio + self.geratriz)

    def volume(self):
        self.conferir()
        return (1 / 3) * math.pi * self.raio**2 * self.altura
