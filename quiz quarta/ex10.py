import string

def calcular_frequencia_palavras(texto):
    # Remove pontuações do texto e o transforma em minúsculas
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Divide o texto em palavras
    palavras = texto_limpo.split()
    
    # Dicionário para armazenar a frequência das palavras
    frequencia_palavras = {}
    
    # Conta a frequência de cada palavra
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else:
            frequencia_palavras[palavra] = 1
            
    return frequencia_palavras

# Exemplo de uso
texto = "Este é um exemplo de texto. Este texto contém algumas palavras repetidas, como texto e exemplo."
frequencias = calcular_frequencia_palavras(texto)

for palavra, frequencia in frequencias.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vezes.")
