import math
from abc import ABC, abstractmethod

# Classe Base
class Prisma(ABC):
    def __init__(self, H):
        self.H = H  # Altura do prisma

    def volume_prisma(self):
        A_base = self.area_base()  # Área da base do prisma
        Volume = A_base * self.H  # Volume = área da base * altura
        return Volume

    def area_prisma(self):
        A_base = self.area_base()  # Área da base
        A_lateral = self.area_lateral()  # Área lateral
        return 2 * A_base + A_lateral  # Área total (2 * área base + área lateral)

    @abstractmethod
    def area_base(self):
        pass

    @abstractmethod
    def area_lateral(self):
        pass


# Classe para Prisma Retangular
class BaseRetangular(Prisma):
    def __init__(self, L1, L2, H):
        super().__init__(H)  # Chama o construtor da classe base
        self.L1 = L1  # Lado 1 da base
        self.L2 = L2  # Lado 2 da base
        # O terceiro lado da base é redundante em um retângulo, por isso não precisa ser fornecido

    def area_base(self):
        return self.L1 * self.L2  # Área da base (L1 * L2 para um retângulo)

    def area_lateral(self):
        return 2 * (self.L1 * self.H) + 2 * (self.L2 * self.H)  # Área lateral (perímetros dos lados multiplicados pela altura)


# Classe para Prisma Triangular
class BaseTriangular(Prisma):
    def __init__(self, L1, L2, L3, H):
        super().__init__(H)  # Chama o construtor da classe base
        self.L1 = L1  # Lado 1 da base
        self.L2 = L2  # Lado 2 da base
        self.L3 = L3  # Lado 3 da base

    def area_base(self):
        S = (self.L1 + self.L2 + self.L3) / 2  # Semi-perímetro
        return math.sqrt(S * (S - self.L1) * (S - self.L2) * (S - self.L3))  # Fórmula de Herão para a área da base triangular

    def area_lateral(self):
        return (self.L1 * self.H) + (self.L2 * self.H) + (self.L3 * self.H)  # Área lateral (perímetros dos lados multiplicados pela altura)
