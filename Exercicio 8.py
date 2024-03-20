#(8) Implemente a função `todos_iguais(sequencia)` que retorna `True` se todos os elementos de `sequencia` forem iguais, e retorna `False` caso contrário.

def todos_iguais(sequencia):
    # Função para verificar se todos os elementos em uma sequência são iguais
    elem = sequencia[0]  # Atribui o primeiro elemento da sequência a uma variável 'elem'
    for item in sequencia:  # Itera sobre cada elemento na sequência
        if elem != item:  # Verifica se o elemento atual é diferente do primeiro elemento
            return False  # Se forem diferentes, retorna False, indicando que nem todos os elementos são iguais
    return True  # Se todos os elementos forem iguais ao primeiro elemento, retorna True

# Exemplo de uso da função todos_iguais()
sequencia = [1, 1, 1, 1, 1]  # Sequência em que todos os elementos são iguais
print(todos_iguais(sequencia))  # Deve retornar True, pois todos os elementos são iguais

sequencia = [1, 2, 3, 4, 5]  # Sequência em que nem todos os elementos são iguais
print(todos_iguais(sequencia))  # Deve retornar False, pois nem todos os elementos são iguais
