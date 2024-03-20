#Implemente a função `maiorN(lista, N)` que recebe uma lista de números quaisquer, um valor `N`, `1 <= N <= len(lista)`,  e retorna o Nésimo maior valor na lista de números. Por exemplo, se `N` for `1`, retorna o maior valor na lista, se `N` for `2`, retorna o segundo maior valor na lista, etc. Exemplo:
#lista = [5, -1, 7, 0, -3, 9]
#N = 2
#print(f'Em {lista} o {N}o. maior valor é {maiorN(lista, N)}')

def maiorN(lista, N):
    # Função para encontrar o N-ésimo maior valor em uma lista
    if not 1 <= N <= len(lista):  # Verifica se N está dentro do intervalo válido
        print(f'Valor de N ({N}) inadequado')  # Se N estiver fora do intervalo, imprime uma mensagem de erro
        return None  # Retorna None, indicando um valor inválido de N
    listaN = lista[:]  # Cria uma cópia da lista original para evitar modificar a lista original
    listaN.sort()  # Ordena a lista em ordem crescente
    listaN.reverse()  # Inverte a ordem da lista, tornando-a em ordem decrescente
    return listaN[N - 1]  # Retorna o N-ésimo maior valor da lista

# Define a lista e o valor de N
lista = [5, -1, 7, 0, -3, 9]
N = 2

# Chama a função maiorN() com a lista e N especificados e imprime o resultado
print(f'Em {lista} o {N}o. maior valor é {maiorN(lista, N)}')
