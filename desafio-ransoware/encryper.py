import os
from cryptography.fernet import Fernet

def gerar_chave():
    """Gera e salva uma chave de criptografia em um arquivo chave.key."""
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    """Carrega a chave de criptografia do arquivo chave.key."""
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

def criptografar_arquivos(diretorio):
    """Criptografa todos os arquivos no diretório especificado."""
    chave = carregar_chave()
    fernet = Fernet(chave)

    for root, _, files in os.walk(diretorio):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            with open(caminho_arquivo, "rb") as arquivo:
                conteudo = arquivo.read()
            conteudo_criptografado = fernet.encrypt(conteudo)
            with open(caminho_arquivo, "wb") as arquivo:
                arquivo.write(conteudo_criptografado)

if __name__ == "__main__":
    gerar_chave()
    diretorio_alvo = input("Digite o diretório que deseja criptografar: ")
    criptografar_arquivos(diretorio_alvo)
    print("Arquivos criptografados com sucesso!")

