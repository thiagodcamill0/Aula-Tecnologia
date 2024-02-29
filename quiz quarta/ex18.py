import csv

def mes_menos_vendas(caminho_arquivo):
    mes_menor_venda = ''
    valor_menor_venda = float('inf')  # Inicializa com infinito para garantir que qualquer valor seja menor
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            mes, vendas = linha
            vendas = float(vendas)
            if vendas < valor_menor_venda:
                mes_menor_venda = mes
                valor_menor_venda = vendas
    return mes_menor_venda

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.csv'
print(mes_menos_vendas(caminho))
