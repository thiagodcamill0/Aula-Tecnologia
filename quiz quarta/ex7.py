def intersecao_listas(lista1, lista2):
    intersecao = []  # Lista para armazenar a interseção

    for elemento in lista1:
        if elemento in lista2 and elemento not in intersecao:
            intersecao.append(elemento)

    return intersecao

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print(intersecao_listas(lista1, lista2))
