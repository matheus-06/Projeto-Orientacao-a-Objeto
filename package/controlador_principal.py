from .controladores.controlador_prismas import ControladorPrismas
from .controladores.controlador_solidos import ControladorSolidos
from .controladores.controlador_matrizes import ControladorMatrizes

class ControladorPrincipal:
    def __init__(self):
        self.opcoes = {
            "1": ControladorPrismas(),
            "2": ControladorSolidos(),
            "3": ControladorMatrizes()
        }

    def exibir_menu(self):
        print("\n=== MENU PRINCIPAL ===")
        print(" 1 : Cálculo de Prismas")
        print(" 2 : Cálculo de Sólidos de Revolução")
        print(" 3 : Cálculo de Matrizes")
        print("-1 : Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")
            
            if escolha == "-1":
                print("Encerrando o programa...")
                break
            elif escolha in self.opcoes:
                self.opcoes[escolha].executar()
            else:
                print("Opção inválida. Tente novamente.")
