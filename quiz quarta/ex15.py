import json

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
        # Carrega o conteúdo do arquivo JSON para um dicionário Python
        dados = json.load(arquivo_json)
    return dados

# Exemplo de uso
caminho = 'caminho_para_seu_arquivo.json'
dados_json = ler_arquivo_json(caminho)

# Imprime os dados lidos para verificar
print(json.dumps(dados_json, indent=4))
