def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(lista):
    """Retorna uma lista de números primos a partir da lista fornecida."""
    primos = [num for num in lista if eh_primo(num)]
    return primos

# Exemplo de uso
lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
numeros_primos = encontrar_primos(lista_numeros)
print("Números primos na lista:", numeros_primos)
