import numpy as np
from abc import ABC, abstractmethod

# Decorador
def requer_matriz_quadrada(func):
    def wrapper(self, *args, **kwargs):
        if self.linhas != self.colunas:
            raise ValueError("\033[31mA matriz deve ser quadrada para realizar esta operação.\033[0m")
        return func(self, *args, **kwargs)
    return wrapper

def verificar_matriz_vazia(matriz):
     if matriz.matriz is None or matriz.matriz.size == 0:
        raise ValueError("\033[31mErro: A matriz está vazia.\033[0m")

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
        while True:
            self.linhas = int(input("Número de Linhas: "))
            self.colunas = int(input("Número de Colunas: "))
            if self.linhas <= 0 or self.colunas <= 0:
                print("\033[31mO numero de colunas e linhas deve ser maior que zero\033[0m")
            else:
                break
        print("Digite os elementos da Matriz (Separe com espaço):")
        elementos = list(map(float, input().split()))
        
        
        if len(elementos) != self.linhas * self.colunas:
            raise ValueError("\033[31mO número de elementos não corresponde ao número de colunas.\033[0m")
        
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
        try:
            matriz_transposta = self.matriz.T
            print("Matriz Transposta:")
            print(matriz_transposta)
        except AttributeError as e:
            print(f"\033[31mErro: A operação de transposição falhou. {e}\033[0m")
            print("\033[31mTente escrever a matriz novamente\033[0m")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    def inversa(self):
        try:
            matriz_inversa = np.linalg.inv(self.matriz)
            print("Matriz Inversa:")
            print(matriz_inversa)
        except np.linalg.LinAlgError:
            print("\033[31mA matriz é singular ou não é quadrada, logo não possui inversa.\033[0m")

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
