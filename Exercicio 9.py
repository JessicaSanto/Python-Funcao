#(9) Implemente a função `todos_diferentes(sequencia)` que retorna `True` se todos os elementos de `sequencia` forem diferentes entre si, e retorna `False` caso contrário, isto é, pelos menos um elemento seja igual a outro componente da `sequencia`.

def todos_diferentes(sequencia):
    # Função para verificar se todos os elementos em uma sequência são diferentes
    seq = sequencia[:]  # Cria uma cópia da sequência original para não modificar a sequência original
    seq.sort()  # Ordena a sequência para facilitar a detecção de elementos repetidos
    N = len(seq)  # Obtém o tamanho da sequência ordenada
    for idx in range(N - 1):  # Itera sobre os índices da sequência (exceto o último)
        if seq[idx] == seq[idx + 1]:  # Verifica se o elemento atual é igual ao próximo elemento
            return False  # Se encontrar dois elementos iguais consecutivos, retorna False
    return True  # Se nenhum par de elementos iguais for encontrado, retorna True, indicando que todos os elementos são diferentes
