from ..modelos.prisma import BaseRetangular, BaseTriangular

class ControladorPrismas:
    def executar(self):
        print("\n=== CÁLCULO DE PRISMAS ===")
        print("1 - Prisma Retangular")
        print("2 - Prisma Triangular")
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            self.calcular_prisma_retangular()
        elif escolha == "2":
            self.calcular_prisma_triangular()
        else:
            print("Opção inválida.")
    
    def calcular_prisma_retangular(self):
        l1 = float(input("Digite o lado 1 da base: "))
        l2 = float(input("Digite o lado 2 da base: "))
        h = float(input("Digite a altura do prisma: "))
        prisma = BaseRetangular(l1, l2, h)
        print(f"Área: {prisma.area_prisma():.2f}, Volume: {prisma.volume_prisma():.2f}")
    
    def calcular_prisma_triangular(self):
        l1 = float(input("Digite o lado 1 da base: "))
        l2 = float(input("Digite o lado 2 da base: "))
        l3 = float(input("Digite o lado 3 da base: "))
        h = float(input("Digite a altura do prisma: "))
        prisma = BaseTriangular(l1, l2, l3, h)
        print(f"Área: {prisma.area_prisma():.2f}, Volume: {prisma.volume_prisma():.2f}")
