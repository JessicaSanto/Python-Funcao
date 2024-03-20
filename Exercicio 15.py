# (15) Implemente uma função que recebe o seu peso e altura e retorna seu índice de massa corporal, IMC. A função também deverá emitir a classificação, de acordo com a tabela abaixo:

# IMC|CLASSIFICAÇÃO
# ---|-------------
# MENOR QUE 18,5|	MAGREZA
# ENTRE 18,5 E 25,0|	NORMAL
# ENTRE 25,0 E 30,0|	SOBREPESO
# ENTRE 30,0 E 40,0|	OBESIDADE
# MAIOR QUE 40,0|	OBESIDADE GRAVE

# Dica:
# \text{IMC} = \frac{\text{peso}}{\text{altura}^2} \text{  , peso em kg, altura em m}


def imc(peso, altura):
    # Calcula o IMC (Índice de Massa Corporal) usando a fórmula peso / altura^2
    imc = peso / altura**2
    # Imprime o valor do IMC formatado com uma casa decimal
    print(f'IMC = {imc:.1f}')
    # Imprime a classificação do IMC com base nos valores de referência
    print(f'Classificação = ', end='')
    if imc > 40.0:
        print('Obesidade grave')
    elif imc > 30:
        print('Obesidade')
    elif imc > 25.0:
        print('Sobrepeso')
    elif imc > 18.5:
        print('Normal')
    else:
        print('Magreza')

# Define os valores de peso e altura
peso, altura = 59, 1.64
# Chama a função imc() com os valores de peso e altura definidos e imprime o resultado
imc(peso, altura)
