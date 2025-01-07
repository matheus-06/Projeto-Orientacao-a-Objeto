from ..modelos.Solidos import Cilindro, Cone, Esfera

class ControladorSolidos:
    def executar(self):
        print("\n=== CÁLCULO DE SÓLIDOS DE REVOLUÇÃO ===")
        print("1 - Cilindro")
        print("2 - Cone")
        print("3 - Esfera")
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            self.calcular_cilindro()
        elif escolha == "2":
            self.calcular_cone()
        elif escolha == "3":
            self.calcular_esfera()
        else:
            print("Opção inválida.")
#---------------------------------------------------------
    def calcular_cilindro(self):
        try:
            altura = float(input("Digite a altura do cilindro: "))
            raio = float(input("Digite o raio do cilindro: "))
            cilindro = Cilindro(altura, raio)
            print(f"Altura do cilindro: {cilindro.get_altura()}")
            print(f"Raio do cilindro: {cilindro.get_raio()}")
            print(f"Área: {cilindro.area():.2f}, Volume: {cilindro.volume():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
#---------------------------------------------------------
    def calcular_cone(self):
        try:
            altura = float(input("Digite a altura do cone (se não souber, digite 0): "))
            raio = float(input("Digite o raio do cone (se não souber, digite 0): "))
            geratriz = float(input("Digite a geratriz do cone (se não souber, digite 0): "))
    
            cone = Cone(altura, raio, geratriz)
            cone.conferir()
        
            if cone.conferir_existencia() != False:
                print(f"Altura: {cone.get_altura():.2f}")
                print(f"Raio: {cone.get_raio():.2f}")
                print(f"Geratriz: {cone.get_geratriz():.2f}")
                print(f"Área: {cone.area():.2f}, Volume: {cone.volume():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
#---------------------------------------------------------
    def calcular_esfera(self):
        try:
            raio = float(input("Digite o raio da esfera: "))
            esfera = Esfera(raio)

            print(f"Raio: {esfera.get_raio():.2f}")
            print(f"Área: {esfera.area():.2f}, Volume: {esfera.volume():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
