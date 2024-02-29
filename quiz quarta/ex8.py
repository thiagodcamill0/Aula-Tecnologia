import random

def embaralhar_lista(lista):
    n = len(lista)
    for i in range(n-1, 0, -1):
        # Escolhe um índice aleatório de 0 a i
        j = random.randint(0, i)
        
        # Troca o elemento atual pelo elemento no índice aleatório
        lista[i], lista[j] = lista[j], lista[i]
    return lista

# Exemplo de uso
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_embaralhada = embaralhar_lista(lista_original.copy())  # Usar copy() para não modificar a lista original
print("Lista original:", lista_original)
print("Lista embaralhada:", lista_embaralhada)
