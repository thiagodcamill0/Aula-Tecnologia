def ler_arquivo_completo(caminho_arquivo):
    # Abrir o arquivo para leitura ('r')
    with open(caminho_arquivo, 'r') as arquivo:
        # Ler todo o conteúdo do arquivo
        conteudo = arquivo.read()
    return conteudo

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.txt'
conteudo_arquivo = ler_arquivo_completo(caminho)
print(conteudo_arquivo)
