import csv

def soma_vendas_por_vendedor(caminho_arquivo):
    vendas_por_vendedor = {}
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            vendedor, valor_venda = linha
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += float(valor_venda)
            else:
                vendas_por_vendedor[vendedor] = float(valor_venda)
    return vendas_por_vendedor

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.csv'
vendas = soma_vendas_por_vendedor(caminho)
for vendedor, soma in vendas.items():
    print(f"Vendedor: {vendedor}, Soma das vendas: {soma}")
