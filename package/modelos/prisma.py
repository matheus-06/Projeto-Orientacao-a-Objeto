import math
from abc import ABC, abstractmethod

# Classe Base para Prisma
class Prisma(ABC):
    def __init__(self, H):
        self.H = H  # Altura do prisma

    def volume_prisma(self):
        return self.area_base() * self.H

    def area_prisma(self):
        return 2 * self.area_base() + self.area_lateral()

    @abstractmethod
    def area_base(self):
        pass

    @abstractmethod
    def area_lateral(self):
        pass

# Prisma Retangular
class BaseRetangular(Prisma):
    def __init__(self, L1, L2, H):
        super().__init__(H)
        self.L1 = L1
        self.L2 = L2

    def area_base(self):
        return self.L1 * self.L2

    def area_lateral(self):
        return 2 * (self.L1 + self.L2) * self.H

# Prisma Triangular
class BaseTriangular(Prisma):
    def __init__(self, L1, L2, L3, H):
        super().__init__(H)
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def teste_base_triangular(self):
        if (self.L1 + self.L2 > self.L3) and (self.L1 + self.L3 > self.L2) and (self.L2 + self.L3 > self.L1):
            return 1
        else:
            return -1        

    def area_base(self):
        s = (self.L1 + self.L2 + self.L3) / 2
        return math.sqrt(s * (s - self.L1) * (s - self.L2) * (s - self.L3))
       
    def area_lateral(self):
        return (self.L1 + self.L2 + self.L3) * self.H
