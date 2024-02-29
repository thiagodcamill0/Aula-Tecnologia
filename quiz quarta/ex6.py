def soma_matrizes(matriz_a, matriz_b):
    # Verificar se as matrizes têm o mesmo tamanho
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        return "As matrizes devem ter o mesmo tamanho para serem somadas."

    # Criar uma nova matriz para armazenar o resultado da soma
    matriz_soma = [[0 for coluna in range(len(matriz_a[0]))] for linha in range(len(matriz_a))]

    # Percorrer cada elemento das matrizes
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[0])):
            matriz_soma[i][j] = matriz_a[i][j] + matriz_b[i][j]

    return matriz_soma

# Exemplo de uso
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

soma = soma_matrizes(matriz_a, matriz_b)
for linha in soma:
    print(linha)
