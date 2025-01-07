from package.controlador_principal import ControladorPrincipal
import os
import atexit

# Função para limpar arquivos .pkl
def limpar_arquivos_pkl():
    # Diretório onde os arquivos .pkl estão localizados (atual diretório, por exemplo)
    diretorio = os.getcwd()  # Pode ser alterado para o caminho onde os arquivos estão
    
    # Percorre todos os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith('.pkl'):
            # Remove os arquivos .pkl
            os.remove(os.path.join(diretorio, filename))
            print(f"Arquivo {filename} removido.")

# Registra a função para ser chamada quando o programa terminar
atexit.register(limpar_arquivos_pkl)
def main():
    controlador = ControladorPrincipal()
    controlador.executar()

if __name__ == "__main__":
    main()
