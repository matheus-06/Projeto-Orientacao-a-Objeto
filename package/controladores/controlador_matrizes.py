from ..modelos.matriz import Matriz, verificar_matriz_vazia
class ControladorMatrizes:
    def __init__(self):
        self.matriz = Matriz()

    def executar(self):
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
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.determinante()
                    except ValueError as e:
                        print(e)

                elif escolha == 3:
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.transposta()
                    except ValueError as e:
                        print(e)
                elif escolha == 4:
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.inversa()
                    except ValueError as e:
                        print(e)
                elif escolha == 5:
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.cofatores()
                    except ValueError as e:
                        print(e)
                elif escolha == 6:
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.adjunta()
                    except ValueError as e:
                        print(e)
                elif escolha == 7:
                    try:
                        verificar_matriz_vazia(self.matriz)
                        self.matriz.escalonada()
                    except ValueError as e:
                        print(e)
                    
                else:
                    print("\033[31mOpção inválida!\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida, por favor insira um número válido.\033[0m")

