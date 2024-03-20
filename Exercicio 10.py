#(10) Implemente uma função que recebe como argumentos um número `n` e uma lista de números, `indice_elemento(n, lista)`. A função retornará o índice da primeira ocorrênia do número na lista e `-1` se o número não estiver na lista. Obs: em Python, índices de listas, arrays, etc. começam em `0`.

def indice_elemento(n, lista):
    # Função para encontrar o índice de um elemento 'n' em uma lista
    for idx, num in enumerate(lista):  # Itera sobre os índices e elementos da lista simultaneamente
        if n == num:  # Verifica se o elemento atual é igual a 'n'
            return idx  # Se 'n' for encontrado na lista, retorna o índice desse elemento
    return -1  # Se 'n' não for encontrado na lista, retorna -1

# Testa a função indice_elemento() com diferentes valores e listas e imprime os resultados
print(indice_elemento(-1, [-1, 7, 1, 10]))  # Deve retornar 0, pois o valor -1 está na posição 0 da lista
print(indice_elemento(1, [-1, 7, 1, 10]))   # Deve retornar 2, pois o valor 1 está na posição 2 da lista
print(indice_elemento(10, [-1, 7, 1, 10]))  # Deve retornar 3, pois o valor 10 está na posição 3 da lista
print(indice_elemento(2, [-1, 7, 1, 10]))   # Deve retornar -1, pois o valor 2 não está na lista
