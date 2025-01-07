from Tentativa2Matriz import Matriz  # Importando a classe Matriz
from Prismas import BaseRetangular, BaseTriangular  # Importando as classes de Prisma
from Cilindro import Cilindro  # Importando a classe Cilindro
from Cone import Cone  # Importando a classe Cone
from Esfera import Esfera  # Importando a classe Esfera

class Controlador:
    def __init__(self):
        self.matriz = Matriz()
        self.prisma = None

    def menu(self):
        while True:
            print("\nEscolha o tipo de operação:")
            print("\t1: Operações com Matrizes")
            print("\t2: Cálculos de Prismas")
            print("\t3: Cálculos de Cilindro, Cone e Esfera")
            print("\t-1: Sair")

            try:
                escolha = int(input("Digite a opção desejada: "))
                if escolha == -1:
                    print("Saindo...")
                    break
                elif escolha == 1:
                    self.menu_matriz()
                elif escolha == 2:
                    self.menu_prisma()
                elif escolha == 3:
                    self.menu_formas()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida, por favor insira um número válido.")

    # Métodos de Matrizes
    def menu_matriz(self):
        while True:
            print("\nEscolha uma operação com Matrizes:")
            print("\t0: Ler Matriz")
            print("\t1: Determinante")
            print("\t2: Transposta")
            print("\t3: Inversa")
            print("\t4: Cofatores")
            print("\t5: Adjunta")
            print("\t6: Escalonada")
            print("\t-1: Voltar")

            try:
                modo = int(input("Digite a opção desejada: "))
                if modo == -1:
                    break
                elif modo == 0:
                    self.matriz.ler_matriz()
                elif modo == 1:
                    self.matriz.determinante()
                elif modo == 2:
                    self.matriz.transposta()
                elif modo == 3:
                    self.matriz.inversa()
                elif modo == 4:
                    self.matriz.cofatores()
                elif modo == 5:
                    self.matriz.adjunta()
                elif modo == 6:
                    self.matriz.escalonada()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida, por favor insira um número válido.")

    # Métodos de Prismas
    def menu_prisma(self):
        while True:
            print("\nEscolha o tipo de Prisma:")
            print("\t1: Calcular Prisma Retangular")
            print("\t2: Calcular Prisma Triangular")
            print("\t-1: Voltar")

            try:
                modo = int(input("Digite a opção desejada: "))
                if modo == -1:
                    break
                elif modo == 1:
                    self.calcular_prisma_retangular()
                elif modo == 2:
                    self.calcular_prisma_triangular()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida, por favor insira um número válido.")

    def calcular_prisma_retangular(self):
        print("\nDigite os parâmetros do Prisma Retangular:")
        L1 = float(input("Lado 1 da base: "))
        L2 = float(input("Lado 2 da base: "))
        H = float(input("Altura: "))
        prisma = BaseRetangular(L1, L2, H)
        print(f"\nÁrea da Base: {prisma.area_base()}")
        print(f"Área Total do Prisma: {prisma.area_prisma()}")
        print(f"Volume do Prisma: {prisma.volume_prisma()}")

    def calcular_prisma_triangular(self):
        print("\nDigite os parâmetros do Prisma Triangular:")
        L1 = float(input("Lado 1 da base: "))
        L2 = float(input("Lado 2 da base: "))
        L3 = float(input("Lado 3 da base: "))
        H = float(input("Altura: "))
        prisma = BaseTriangular(L1, L2, L3, H)
        print(f"\nÁrea da Base: {prisma.area_base()}")
        print(f"Área Total do Prisma: {prisma.area_prisma()}")
        print(f"Volume do Prisma: {prisma.volume_prisma()}")

    # Métodos de Cilindro, Cone e Esfera
    def menu_formas(self):
        while True:
            print("\nEscolha uma forma geométrica:")
            print("\t1: Cilindro")
            print("\t2: Cone")
            print("\t3: Esfera")
            print("\t-1: Voltar")

            try:
                escolha = int(input("Digite a opção desejada: "))
                if escolha == -1:
                    break
                elif escolha == 1:
                    self.calcular_cilindro()
                elif escolha == 2:
                    self.calcular_cone()
                elif escolha == 3:
                    self.calcular_esfera()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida, por favor insira um número válido.")

    def calcular_cilindro(self):
        print("\nDigite os parâmetros do Cilindro:")
        H = float(input("Altura (H): "))
        r = float(input("Raio (r): "))
        cilindro = Cilindro(H, r)
        print(f"\nÁrea: {cilindro.area():.2f}")
        print(f"Volume: {cilindro.volume():.2f}")

    def calcular_cone(self):
        print("\nDigite os parâmetros do Cone (digite '0' se desconhecido):")
        H = float(input("Altura (H): "))
        r = float(input("Raio (r): "))
        G = float(input("Geratriz (G): "))
        cone = Cone(H, r, G)
        cone.conferir()
        print(f"\nÁrea: {cone.area():.2f}")
        print(f"Volume: {cone.volume():.2f}")

    def calcular_esfera(self):
        print("\nDigite o raio da Esfera:")
        r = float(input("Raio (r): "))
        esfera = Esfera(r)
        print(f"\nÁrea: {esfera.area():.2f}")
        print(f"Volume: {esfera.volume():.2f}")

# Execução
if __name__ == "__main__":
    controlador = Controlador()
    controlador.menu()
