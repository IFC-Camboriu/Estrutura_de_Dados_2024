import numpy as np

# define o tamanho do array
N = 5
#preenche a estrutura com zeros
matriz = np.zeros((N,N))

#mostra a matriz
print(matriz)

# Preenche a matriz conforme as condições dadas
for i in range(N):
    for j in range(N):
        if i < j:
            matriz[i][j] = (2 * i) + (7 * j)
        elif i == j:
            matriz[i][j] = (3 * (i ** 2))
        else:
            matriz[i][j] = (4 * (i ** 3)) + (5 * (j ** 2)) + 1

# Imprime a matriz resultante
print("Matriz Resultante:")
for linha in matriz:
    print(linha)