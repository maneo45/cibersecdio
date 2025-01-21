import os
from cryptography.fernet import Fernet

def carregar_chave():
    """Carrega a chave de criptografia do arquivo chave.key."""
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

def descriptografar_arquivos(diretorio):
    """Descriptografa todos os arquivos no diretório especificado."""
    chave = carregar_chave()
    fernet = Fernet(chave)

    for root, _, files in os.walk(diretorio):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            with open(caminho_arquivo, "rb") as arquivo:
                conteudo_criptografado = arquivo.read()
            conteudo_original = fernet.decrypt(conteudo_criptografado)
            with open(caminho_arquivo, "wb") as arquivo:
                arquivo.write(conteudo_original)

if __name__ == "__main__":
    diretorio_alvo = input("Digite o diretório que deseja descriptografar: ")
    descriptografar_arquivos(diretorio_alvo)
    print("Arquivos descriptografados com sucesso!")

