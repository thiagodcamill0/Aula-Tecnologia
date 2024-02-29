import csv

def ler_arquivo_csv(caminho_arquivo):
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabecalho = next(leitor_csv)  # Lê o cabeçalho, se houver
        print(f'Cabeçalho: {cabecalho}')
        for linha in leitor_csv:
            print(linha)

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.csv'
ler_arquivo_csv(caminho)
