import numpy as np
from abc import ABC, abstractmethod

# Decorador para verificar se a matriz é quadrada
def requer_matriz_quadrada(func):
    def wrapper(self, *args, **kwargs):
        if self.linhas != self.colunas:
            raise ValueError("A matriz deve ser quadrada para realizar esta operação.")
        return func(self, *args, **kwargs)
    return wrapper

# Classe base abstrata
class BaseMatriz(ABC):
    @abstractmethod
    def determinante(self):
        pass

    @abstractmethod
    def transposta(self):
        pass

# Classe Matriz
class Matriz(BaseMatriz):
    def __init__(self):
        self.linhas = 0
        self.colunas = 0
        self.matriz = None

    def ler_matriz(self):
        self.linhas = int(input("Número de Linhas: "))
        self.colunas = int(input("Número de Colunas: "))
        print("Digite os elementos da Matriz (Separe com espaço):")
        elementos = list(map(float, input().split()))
        
        # Garantindo que o número de elementos corresponde ao tamanho da matriz
        if len(elementos) != self.linhas * self.colunas:
            raise ValueError("O número de elementos não corresponde ao número de colunas.")
        
        self.matriz = np.array(elementos).reshape(self.linhas, self.colunas)
        self.exibir()

    def exibir(self):
        print("Matriz:")
        print(self.matriz)

    # Métodos de operação
    @requer_matriz_quadrada
    def determinante(self):
        determinante = np.linalg.det(self.matriz)
        print(f"Determinante = {determinante:.2f}")

    def transposta(self):
        matriz_transposta = self.matriz.T
        print("Matriz Transposta:")
        print(matriz_transposta)

    def inversa(self):
        try:
            matriz_inversa = np.linalg.inv(self.matriz)
            print("Matriz Inversa:")
            print(matriz_inversa)
        except np.linalg.LinAlgError:
            print("A matriz é singular ou não é quadrada, logo não possui inversa.")

    @requer_matriz_quadrada
    def cofatores(self):
        cofatores = np.zeros((self.linhas, self.colunas))
        for i in range(self.linhas):
            for j in range(self.colunas):
                menor = np.delete(np.delete(self.matriz, i, axis=0), j, axis=1)
                cofatores[i, j] = ((-1) ** (i + j)) * np.linalg.det(menor)
        print("Matriz de Cofatores:")
        print(cofatores)
        return cofatores

    def adjunta(self):
        cofatores = self.cofatores()
        adjunta = cofatores.T
        print("Matriz Adjunta:")
        print(adjunta)

    def escalonada(self):
        matriz_escalonada = np.array(self.matriz, dtype=float)
        linhas, colunas = matriz_escalonada.shape
        for i in range(min(linhas, colunas)):
            max_index = np.argmax(abs(matriz_escalonada[i:, i])) + i
            if matriz_escalonada[max_index, i] == 0:
                continue
            matriz_escalonada[[i, max_index]] = matriz_escalonada[[max_index, i]]
            matriz_escalonada[i] = matriz_escalonada[i] / matriz_escalonada[i, i]
            for j in range(i + 1, linhas):
                matriz_escalonada[j] -= matriz_escalonada[j, i] * matriz_escalonada[i]
        print("Matriz Escalonada:")
        print(matriz_escalonada)
