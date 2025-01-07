import math

class Esfera:
    def __init__(self, raio):
        self.raio = raio

    # Getters e Setters
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
        return 4 * math.pi * self.raio**2

    def volume(self):
        return (4 / 3) * math.pi * self.raio**3
