import csv

def mes_mais_vendas(caminho_arquivo):
    mes_maior_venda = ''
    valor_maior_venda = 0
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            mes, vendas = linha
            vendas = float(vendas)
            if vendas > valor_maior_venda:
                mes_maior_venda = mes
                valor_maior_venda = vendas
    return mes_maior_venda

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.csv'
print(mes_mais_vendas(caminho))
