from ..modelos.prisma import BaseRetangular, BaseTriangular

class ControladorPrismas:
    def executar(self):
        while True:
            print("\n=== CÁLCULO DE PRISMAS ===")
            print(" 1 : Prisma Retangular")
            print(" 2 : Prisma Triangular")
            print("-1 : Sair")
            
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                self.calcular_prisma_retangular()
            elif escolha == 2:
                self.calcular_prisma_triangular()
            elif escolha == -1:
                break
            else:
                print("\033[31mOpção inválida.\033[0m")
    
    def calcular_prisma_retangular(self):
        try:
            l1 = float(input("Digite o lado 1 da base: "))
            l2 = float(input("Digite o lado 2 da base: "))
            h = float(input("Digite a altura do prisma: "))
            prisma = BaseRetangular(l1, l2, h)
            print(f"Área: {prisma.area_prisma():.2f}, Volume: {prisma.volume_prisma():.2f}")
        except ValueError as e:
            print(f"\033[31mErro: {e}\033[0m")
    def calcular_prisma_triangular(self):
        try:
            l1 = float(input("Digite o lado 1 da base: "))
            l2 = float(input("Digite o lado 2 da base: "))
            l3 = float(input("Digite o lado 3 da base: "))
            h = float(input("Digite a altura do prisma: "))
            prisma = BaseTriangular(l1, l2, l3, h)
            if prisma.teste_base_triangular() == 1:
                print(f"Área: {prisma.area_prisma():.2f}, Volume: {prisma.volume_prisma():.2f}")
            else:
                print("\033[31mErro! A soma de 2 lados deve ser sempre maior que o 3°\033[0m")
        except ValueError as e:
            print(f"\033[31mErro: {e}\033[0m")