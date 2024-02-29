def contar_vogais(s):
    # Lista de vogais
    vogais = 'aeiouAEIOU'
    # Contador inicializado em 0
    contador = 0
    
    # Loop para percorrer cada caractere da string
    for letra in s:
        # Se o caractere for uma vogal, incrementa o contador
        if letra in vogais:
            contador += 1
    
    return contador

# Exemplo de uso
texto = "Exemplo de texto para contagem"
print(contar_vogais(texto))  # Deve imprimir o número de vogais no texto
