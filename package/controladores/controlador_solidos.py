from ..modelos.Solidos import Cilindro, Cone, Esfera
import pickle
import os
import atexit

class ControladorSolidos:
    def __init__(self):
        self.historico = []  # Lista para armazenar os últimos 5 sólidos
    def executar(self):
        while True:
            print("\n=== CÁLCULO DE SÓLIDOS DE REVOLUÇÃO ===")
            print(" 1 : Cilindro")
            print(" 2 : Cone")
            print(" 3 : Esfera")
            print(" 4 : Histórico")
            print("-1 : Sair")
            
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                self.calcular_cilindro()
            elif escolha == 2:
                self.calcular_cone()
            elif escolha == 3:
                self.calcular_esfera()
            elif escolha == 4:
                self.mostrar_historico()
            elif escolha == -1:
                limpar_arquivos_pkl()
                break
            else:
                print("Opção inválida.")
#---------------------------------------------------------
    def calcular_cilindro(self):
        try:
            altura = float(input("Digite a altura do cilindro: "))
            raio = float(input("Digite o raio do cilindro: "))
            cilindro = Cilindro(altura, raio)
            self.adicionar_historico(cilindro)           
            print(f"Altura do cilindro: {cilindro.get_altura()}")
            print(f"Raio do cilindro: {cilindro.get_raio()}")
            print(f"Área: {cilindro.area():.2f}, Volume: {cilindro.volume():.2f}")
        except ValueError as e:
            print(f"\033[31mErro: {e}\033[0m")
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
                self.adicionar_historico(cone)
        except ValueError as e:
            print(f"\033[31mErro: {e}\033[0m")
#---------------------------------------------------------
    def calcular_esfera(self):
        try:
            raio = float(input("Digite o raio da esfera: "))
            esfera = Esfera(raio)

            self.adicionar_historico(esfera)

            print(f"Raio: {esfera.get_raio():.2f}")
            print(f"Área: {esfera.area():.2f}, Volume: {esfera.volume():.2f}")
        except ValueError as e:
            print(f"\033[31mErro: {e}\033[0m")
#------------------------------------------------------------------------------------
    def adicionar_historico(self, solido):
        # Adiciona o sólido ao histórico e mantém apenas os 5 últimos
        if len(self.historico) >= 5:
            self.historico.pop(0)  # Remove o primeiro item se a lista tiver 5 itens
        self.historico.append(solido)
    
    def mostrar_historico(self):
        if not self.historico:
            print("\033[31mNenhum sólido foi calculado ainda.\033[0m")
            return
        print("\033[34m\n*************************************")
        print("=== HISTÓRICO DOS ÚLTIMOS SÓLIDOS ===\n")
        for index, solido in enumerate(self.historico, 1):
            print(f"Sólido {index}: {type(solido).__name__}")
            print(f"Medidas: ")
            if isinstance(solido, Cilindro):
                print(f"  Altura: {solido.get_altura()}, Raio: {solido.get_raio()}")
            elif isinstance(solido, Cone):
                print(f"  Altura: {solido.get_altura()}, Raio: {solido.get_raio()}, Geratriz: {solido.get_geratriz()}")
            elif isinstance(solido, Esfera):
                print(f"  Raio: {solido.get_raio()}")
            print(f"  Área: {solido.area():.2f}, Volume: {solido.volume():.2f}\n")
        print("*************************************\n\033[0m")
#-------------------------------------------------------------------------------------

# Função para limpar arquivos .pkl
def limpar_arquivos_pkl():
    diretorio = os.getcwd()
    for filename in os.listdir(diretorio):
        if filename.endswith('.pkl'):
            os.remove(os.path.join(diretorio, filename))
            print(f"Arquivo {filename} removido.")
# Registra a função para ser chamada quando o programa terminar
atexit.register(limpar_arquivos_pkl)
