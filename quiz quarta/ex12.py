def encontrar_menor_string(lista_strings):
    if not lista_strings:
        return None  # Retorna None se a lista estiver vazia

    # Inicializa a menor string com o primeiro elemento da lista
    menor_string = lista_strings[0]

    # Percorre a lista para encontrar a menor string
    for string in lista_strings[1:]:
        if len(string) < len(menor_string):
            menor_string = string

    return menor_string

# Exemplo de uso
lista_de_strings = ["banana", "maçã", "pêra", "uva", "kiwi"]
menor = encontrar_menor_string(lista_de_strings)
print("A menor string é:", menor)
