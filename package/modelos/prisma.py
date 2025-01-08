import math
from abc import ABC, abstractmethod

# Classe Base para Prisma
class Prisma(ABC):
    def __init__(self, H):
        self.H = H 

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, valor):
        if valor <= 0:
            raise ValueError("H deve ser maior que zero.")
        self._H = valor


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
    def __init__(self, L1 = 0, L2 = 0, H = 0):
        super().__init__(H)
        self._L1 = None
        self._L2 = None
        self.set_L1(L1)
        self.set_L2(L2)
#-------------------------------------------------------
    def get_L1(self):
        return self._L1 
    
    def get_L2(self):
        return self._L2 
    
    def set_L1(self, L1):
        if L1 <= 0:
            raise ValueError("O lado deve ser maior que zero")
        self._L1 = L1
    
    def set_L2(self, L2):
        if L2 <= 0:
            raise ValueError("O lado deve ser maior que zero")
        self._L2 = L2
#-------------------------------------------------------
    def area_base(self):
        return self.get_L1() * self.get_L2()

    def area_lateral(self):
        return 2 * (self.get_L1() + self.get_L2()) * self.H

# Prisma Triangular
class BaseTriangular(Prisma):
    def __init__(self, L1 = 0, L2 = 0, L3 = 0, H = 0):
        super().__init__(H)
        self._L1 = None
        self._L2 = None
        self._L3 = None
        self.set_L1(L1)
        self.set_L2(L2)
        self.set_L3(L3)
#----------------------------------------------------------------
    def teste_base_triangular(self):
        if (self.get_L1() + self.get_L2() > self.get_L3()) and (self.get_L1() + self.get_L3() > self.get_L2()) and (self.get_L2() + self.get_L3() > self.get_L1()):
            return 1
        else:
            return -1   
#----------------------------------------------------------------------
    def get_L1(self):
        return self._L1 
        
    def get_L2(self):
        return self._L2 
        
    def get_L3(self):
        return self._L3 

    def set_L1(self, L1):
        if L1 <= 0:
            raise ValueError("A altura deve ser maior que zero")
        self._L1 = L1
        
    def set_L2(self, L2):
        if L2 <= 0:
            raise ValueError("A altura deve ser maior que zero")
        self._L2 = L2

    def set_L3(self, L3):
        if L3 <= 0:
            raise ValueError("A altura deve ser maior que zero")
        self._L3 = L3
#--------------------------------------------------------------------
    def area_base(self):
        s = (self.get_L1() + self.get_L2() + self.get_L3()) / 2
        return math.sqrt(s * (s - self.get_L1()) * (s - self.get_L2()) * (s - self.get_L3()))
       
    def area_lateral(self):
        return (self.get_L1() + self.get_L2() + self.get_L3()) * self.H
