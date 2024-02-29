import csv

def ler_csv_e_encontrar_vendedores(arquivo_csv):
    vendas_por_vendedor = {}

    # Passo 1: Leitura do arquivo CSV
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pula o cabeçalho se houver um
        for linha in leitor:
            nome, valor_venda = linha
            if nome in vendas_por_vendedor:
                vendas_por_vendedor[nome] += float(valor_venda)
            else:
                vendas_por_vendedor[nome] = float(valor_venda)

    # Passo 2: Identificação dos vendedores
    if vendas_por_vendedor:
        vendedor_mais_vendas = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
        vendedor_menos_vendas = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
        return vendedor_mais_vendas, vendas_por_vendedor[vendedor_mais_vendas], \
               vendedor_menos_vendas, vendas_por_vendedor[vendedor_menos_vendas]
    else:
        return None, None, None, None

# Exemplo de uso
arquivo_csv = 'vendas.csv'  # Substitua pelo caminho do seu arquivo CSV
vendedor_mais, total_mais, vendedor_menos, total_menos = ler_csv_e_encontrar_vendedores(arquivo_csv)
if vendedor_mais:
    print(f"Vendedor que mais vendeu: {vendedor_mais} com um total de R$ {total_mais}")
    print(f"Vendedor que menos vendeu: {vendedor_menos} com um total de R$ {total_menos}")
else:
    print("O arquivo CSV está vazio ou não foi possível processar os dados.")
