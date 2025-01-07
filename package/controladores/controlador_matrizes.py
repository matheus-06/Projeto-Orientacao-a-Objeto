from ..modelos.matriz import Matriz

class ControladorMatrizes:
    def __init__(self):
        # Inicialização das variáveis da classe, como a classe Matriz
        self.matriz = Matriz()

    def executar(self):
        # Aqui você pode implementar o menu ou as opções relacionadas ao controle das matrizes
        while True:
            print("Escolha a operação desejada:")
            print("\t 1: Ler Matriz")
            print("\t 2: Determinante")
            print("\t 3: Transposta")
            print("\t 4: Inversa")
            print("\t 5: Cofatores")
            print("\t 6: Adjunta")
            print("\t 7: Escalonada")
            print("\t-1: Voltar")

            try:
                escolha = int(input("Digite a opção desejada: "))
                if escolha == -1:
                    break
                elif escolha == 1:
                    self.matriz.ler_matriz()
                elif escolha == 2:
                    self.matriz.determinante()
                elif escolha == 3:
                    self.matriz.transposta()
                elif escolha == 4:
                    self.matriz.inversa()
                elif escolha == 5:
                    self.matriz.cofatores()
                elif escolha == 6:
                    self.matriz.adjunta()
                elif escolha == 7:
                    self.matriz.escalonada()
                    
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida, por favor insira um número válido.")

