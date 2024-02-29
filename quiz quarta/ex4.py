def contar_palavras(s):
    # Divide a string em uma lista de palavras
    palavras = s.split()
    # Retorna o número de palavras na lista
    return len(palavras)

# Exemplo de uso
texto = "Este é um exemplo de texto para contagem de palavras."
print(contar_palavras(texto))  # Deve imprimir o número de palavras no texto
