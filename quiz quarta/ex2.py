def substituir_letra(texto, letra_a_substituir, nova_letra):
    # Substitui todas as ocorrências da letra_a_substituir pela nova_letra
    texto_modificado = texto.replace(letra_a_substituir, nova_letra)
    return texto_modificado

# Exemplo de uso
texto_original = "Este é um exemplo de texto para substituição."
letra_a_substituir = "e"
nova_letra = "a"

texto_modificado = substituir_letra(texto_original, letra_a_substituir, nova_letra)
print(texto_modificado)
