import os

def consolidar_arquivos_texto(diretorio, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo_destino:
        for nome_arquivo in os.listdir(diretorio):
            if nome_arquivo.endswith('.txt'):
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                with open(caminho_arquivo, 'r') as arquivo_fonte:
                    conteudo = arquivo_fonte.read()
                    arquivo_destino.write(conteudo)
                    arquivo_destino.write('\n')  # Adiciona uma nova linha entre os arquivos

# Exemplo de uso
diretorio = 'caminho_para_seu_diretorio'
arquivo_saida = 'arquivo_consolidado.txt'
consolidar_arquivos_texto(diretorio, arquivo_saida)
