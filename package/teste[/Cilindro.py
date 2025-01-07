import math

class Cilindro:
    def __init__(self, altura, raio):
        self.altura = altura
        self.raio = raio

    # Getters e Setters
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        self._altura = valor

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self._raio = valor

    # Métodos de cálculo
    def area(self):
        return 2 * math.pi * self.raio * (self.raio + self.altura)

    def volume(self):
        return math.pi * self.raio**2 * self.altura
