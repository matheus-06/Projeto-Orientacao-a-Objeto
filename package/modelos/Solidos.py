import math

# Classe Cilindro
class Cilindro:
    def __init__(self, altura, raio):
        self._altura = None
        self._raio = None
        self.set_altura(altura)
        self.set_raio(raio)
    
    # Getters
    def get_altura(self):
        return self._altura

    def get_raio(self):
        return self._raio

    # Setters
    def set_altura(self, altura):
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        self._altura = altura

    def set_raio(self, raio):
        if raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self._raio = raio


    def area(self):
        return 2 * math.pi * self._raio * (self._raio + self._altura)

    def volume(self):
        return math.pi * self._raio**2 * self._altura
#___________________________________________________________________________
# Classe Cone
class Cone:
    def __init__(self, altura=0, raio=0, geratriz=0):
        self._altura = None
        self._raio = None
        self._geratriz = None
        self.set_altura(altura)
        self.set_raio(raio)
        self.set_geratriz(geratriz)

    # Getters-------------------------------------------------------
    def get_altura(self):
        return self._altura

    def get_raio(self):
        return self._raio

    def get_geratriz(self):
        return self._geratriz

    # Setters-------------------------------------------------------
    def set_altura(self, altura):
        if altura < 0:
            raise ValueError("A altura deve ser maior ou igual a zero.")
        self._altura = altura

    def set_raio(self, raio):
        if raio < 0:
            raise ValueError("O raio deve ser maior ou igual a zero.")
        self._raio = raio

    def set_geratriz(self, geratriz):
        if geratriz < 0:
            raise ValueError("A geratriz deve ser maior ou igual a zero.")
        self._geratriz = geratriz
    #-----------------------------------------------------------------
    def conferir(self):
        if self.get_altura() == 0 and self.get_geratriz() != 0 and self.get_raio() != 0:
            self.set_altura(math.sqrt(self.get_geratriz()**2 - self.get_raio()**2))
        elif self.get_raio() == 0 and self.get_altura() != 0 and self.get_geratriz() != 0:
            self.set_raio(math.sqrt(self.get_geratriz()**2 - self.get_altura()**2))
        elif self.get_geratriz() == 0 and self.get_altura() != 0 and self.get_raio() != 0:
            self.set_geratriz(math.sqrt(self.get_altura()**2 + self.get_raio()**2))

    def conferir_existencia(self):
        if self.get_geratriz() <= self.get_altura() or self.get_geratriz() <= self.get_raio():
            print("Este cone não existe, confira suas medidas!")
            return False
        if self.get_altura() <= 0 or self.get_geratriz() <= 0 or self.get_raio() <= 0:
            print("Este cone não existe, confira suas medidas!")
            return False
        return True

    def area(self):
        self.conferir()  # Verifica e calcula o valor faltante
        return math.pi * self.get_raio() * (self.get_raio() + self.get_geratriz())

    def volume(self):
        return (1 / 3) * math.pi * self.get_raio()**2 * self.get_altura()

#___________________________________________________________________________
# Classe Esfera
class Esfera:
    def __init__(self, raio):
        self._raio = None  # Atributo privado
        self.set_raio(raio)

    # Getter
    def get_raio(self):
        return self._raio

    # Setter
    def set_raio(self, raio):
        if raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self._raio = raio

    def area(self):
        return 4 * math.pi * self.get_raio()**2

    def volume(self):
        return (4 / 3) * math.pi * self.get_raio()**33
