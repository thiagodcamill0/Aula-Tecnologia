def k_maiores_elementos(lista, k):
    # Encontrar os k maiores elementos (pode haver duplicatas, então usamos um conjunto para a comparação)
    k_maiores = sorted(lista, reverse=True)[:k]
    
    # Criar um dicionário para contar a ocorrência dos k maiores elementos
    k_maiores_count = {x: k_maiores.count(x) for x in k_maiores}
    
    resultado = []
    for elemento in lista:
        # Se o elemento está no dicionário e a contagem é positiva, adicione ao resultado
        if elemento in k_maiores_count and k_maiores_count[elemento] > 0:
            resultado.append(elemento)
            # Decrementar a contagem para garantir a ordem original e a quantidade correta
            k_maiores_count[elemento] -= 1
            
    return resultado

# Exemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 4
print(k_maiores_elementos(lista, k))
