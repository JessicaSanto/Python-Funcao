#(12) Implemente uma funçao que dado um número natural maior do que `1`, decomponha esse número em fatores primos. Por exemplo, se o argumento de entrada for 36, a saída deverá ser [2, 2, 3, 3], porque $2 \times 2 \times 3 \times 3 = 36$.

def decompoe(numero):
    # Função para decompor um número em seus fatores primos
    fatores = []  # Inicializa uma lista para armazenar os fatores primos do número
    divisor = 2  # Inicializa o divisor como 2, o menor número primo

    while numero > 1:  # Entra em um loop while enquanto o número for maior que 1
        # Verifica se o divisor é um fator primo do número
        while numero % divisor == 0:  # Entra em um loop while enquanto o número for divisível pelo divisor
            fatores.append(divisor)  # Adiciona o divisor à lista de fatores primos
            numero //= divisor  # Divide o número pelo divisor
        divisor += 1  # Incrementa o divisor para verificar o próximo número primo

    return fatores  # Retorna a lista de fatores primos do número

# Testa a função decompoe() para diferentes valores de 'n' e imprime os resultados
for n in [2, 3, 4, 5, 6, 36]:
    print(decompoe(n))  # Imprime os fatores primos de cada número
