def encontrar_par_soma(lista, valor_soma):
    visitados = set()  # Conjunto para armazenar os elementos já visitados
    for numero in lista:
        complemento = valor_soma - numero
        if complemento in visitados:
            return (complemento, numero)  # Retorna o par encontrado
        visitados.add(numero)
    return None  # Retorna None se nenhum par for encontrado

# Exemplo de uso
lista = [2, 4, 5, 1, 3, 9, 8, 6]
valor_soma = 10

par = encontrar_par_soma(lista, valor_soma)
if par:
    print(f"Par encontrado: {par}")
else:
    print("Nenhum par encontrado.")
